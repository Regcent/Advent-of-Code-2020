import time
from typing import Union

class Cup:

    def __init__(self, label: int, min_label: int, max_label: int):
        self.label = label
        self.previous = max_label if label == min_label else label - 1
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
    pretty_print_cups(cups, 10)
    current_cup_label = int(raw_data[0])
    perform_game(cups, current_cup_label, 1)

def perform_game(cups: list, current_cup_label: int, turns: int) -> None:
    for i in range(turns):
        print(f"\nRound {i}")
        pretty_print_cups(cups, 10)
        print(f"Current cup : {current_cup_label}")
        selected_cups_labels = select_cups(cups, current_cup_label)
        print(f"Selected : {selected_cups_labels}")

def select_cups(cups: list, current_cup_label: int) -> list:
    selected_cups_labels = []
    current_cup = get_labeled_cup(cups, current_cup_label)
    for i in range(3):
        current_cup = get_labeled_cup(cups, current_cup.next)
        selected_cups_labels.append(current_cup.label)
    return selected_cups_labels

def initialize_cups(count: int, raw_data: str, part1: bool) -> list:
    cups = [Cup(i, 1, count) for i in range(1, count + 1)]
    for i in range(1, len(raw_data) - 1):
        current_cup = get_labeled_cup(cups, int(raw_data[i]))
        current_cup.previous = int(raw_data[i-1])
        current_cup.next = int(raw_data[i+1])
    if part1:
        first_cup = get_labeled_cup(cups, int(raw_data[0]))
        first_cup.previous = int(raw_data[-1])
        first_cup.next = int(raw_data[1])
        last_cup = get_labeled_cup(cups, int(raw_data[-1]))
        last_cup.previous = int(raw_data[-2])
        last_cup.next = int(raw_data[0])
    else:
        first_cup = get_labeled_cup(cups, int(raw_data[0]))
        first_cup.previous = count
        first_cup.next = int(raw_data[1])
        last_cup = get_labeled_cup(cups, int(raw_data[-1]))
        last_cup.previous = int(raw_data[-2])
        last_cup.next = len(raw_data)
    return cups

def pretty_print_cups(cups: int, count: int) -> None:
    labels = [str(cups[0].label)]
    current_cup = get_labeled_cup(cups, cups[0].next)
    i = 1
    while not current_cup == cups[0] and i < count:
        labels.append(str(current_cup.label))
        current_cup = get_labeled_cup(cups, current_cup.next)
        i += 1
    print("Cups : " + ", ".join(labels))

def get_labeled_cup(cups: list, label: int) -> Cup:
    return cups[label - 1]

if __name__ == "__main__":
    print(run_script("input.txt"))