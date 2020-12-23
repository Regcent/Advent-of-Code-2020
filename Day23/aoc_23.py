import time
from typing import Union

class Cup:

    def __init__(self, label: int, min_label: int, max_label: int):
        self.label = label
        self.next = min_label if label == max_label else label + 1

def run_script(filepath: str) -> Union[int, str, float, bool]:
    with open(filepath, "r") as f:
        raw_data = f.read()
    return main_function(raw_data)

def main_function(raw_data: str) -> Union[int, str, float, bool]:
    start_time = time.time()
    
    result = your_script(raw_data)

    elapsed_time = time.time() - start_time
    print(f"Time elapsed : {elapsed_time}s")
    return result

def your_script(raw_data: str) -> Union[int, str, float, bool]:
    """
    Time to code! Write your code here to solve today's problem
    """
    cups = initialize_cups(9, raw_data, True)
    current_cup_label = int(raw_data[0])
    perform_game(cups, current_cup_label, 100)
    print(f"Result Part 1 : {prepare_result_1(cups)}")
    cups = initialize_cups(1000000, raw_data, False)
    current_cup_label = int(raw_data[0])
    perform_game(cups, current_cup_label, 10000000)
    print(f"Result Part 2 : {prepare_result_2(cups)}")

def perform_game(cups: list, current_cup_label: int, turns: int) -> None:
    max_label = len(cups)
    for i in range(turns):
        #print(f"\nRound {i+1}")
        #pretty_print_cups(cups, 10)
        #print(f"Current cup : {current_cup_label}")
        selected_cups_labels = select_cups(cups, current_cup_label)
        #print(f"Selected : {selected_cups_labels}")
        destination_label = choose_destination(current_cup_label, selected_cups_labels, max_label)
        #print(f"Destination : {destination_label}")
        perform_transformation(cups, current_cup_label, selected_cups_labels, destination_label)
        current_cup_label = get_labeled_cup(cups, current_cup_label).next

def select_cups(cups: list, current_cup_label: int) -> list:
    selected_cups_labels = []
    current_cup = get_labeled_cup(cups, current_cup_label)
    for i in range(3):
        current_cup = get_labeled_cup(cups, current_cup.next)
        selected_cups_labels.append(current_cup.label)
    return selected_cups_labels

def choose_destination(current_cup_label: int, selected_cups_labels: list, max_label: int) -> int:
    destination_label = current_cup_label - 1
    while destination_label in selected_cups_labels or destination_label <= 0:
        destination_label -= 1
        if destination_label <= 0:
            destination_label = max_label
    return destination_label

def perform_transformation(cups: list, current_cup_label: int, selected_cups_labels: list, destination_label: int) -> None:
    #Remove the selected cups
    last_selected_cup = get_labeled_cup(cups, selected_cups_labels[-1])
    get_labeled_cup(cups, current_cup_label).next = last_selected_cup.next
    #Insert the selected cups
    destination_cup = get_labeled_cup(cups, destination_label)
    destination_neighbor_label = destination_cup.next
    destination_cup.next = selected_cups_labels[0]
    last_selected_cup.next = destination_neighbor_label

def initialize_cups(count: int, raw_data: str, part1: bool) -> list:
    cups = [Cup(i, 1, count) for i in range(1, count + 1)]
    for i in range(1, len(raw_data) - 1):
        current_cup = get_labeled_cup(cups, int(raw_data[i]))
        current_cup.next = int(raw_data[i+1])
    if part1:
        first_cup = get_labeled_cup(cups, int(raw_data[0]))
        first_cup.next = int(raw_data[1])
        last_cup = get_labeled_cup(cups, int(raw_data[-1]))
        last_cup.next = int(raw_data[0])
    else:
        first_cup = get_labeled_cup(cups, int(raw_data[0]))
        first_cup.next = int(raw_data[1])
        last_cup = get_labeled_cup(cups, int(raw_data[-1]))
        last_cup.next = len(raw_data) + 1
        get_labeled_cup(cups, count).next = int(raw_data[0])
    return cups

def pretty_print_cups(cups: list, count: int) -> None:
    labels = [str(cups[0].label)]
    current_cup = get_labeled_cup(cups, cups[0].next)
    i = 1
    while not current_cup == cups[0] and i < count:
        labels.append(str(current_cup.label))
        current_cup = get_labeled_cup(cups, current_cup.next)
        i += 1
    print("Cups : " + ", ".join(labels))

def prepare_result_1(cups: list) -> str:
    labels = []
    current_cup = get_labeled_cup(cups, cups[0].next)
    while not current_cup == cups[0]:
        labels.append(str(current_cup.label))
        current_cup = get_labeled_cup(cups, current_cup.next)
    return "".join(labels)

def prepare_result_2(cups: list) -> str:
    current_label = 1
    total = 1
    for i in range(2):
        current_label = get_labeled_cup(cups, current_label).next
        total *= current_label
    return total

def get_labeled_cup(cups: list, label: int) -> Cup:
    return cups[label - 1]

if __name__ == "__main__":
    print(run_script("input.txt"))