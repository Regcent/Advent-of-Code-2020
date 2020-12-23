import time
from typing import Union

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
    cups = [int(i) for i in raw_data]
    current_cup = cups[0]
    cups = perform_game(cups, current_cup, 100)
    print(f"Part 1 Result : {prepare_result_1(cups)}")
    cups = [int(i) for i in raw_data] + [i for i in range(10, 1000001)]
    current_cup = cups[0]
    cups = perform_game(cups, current_cup, 10)
    print(f"Part 2 Result: {prepare_result_2(cups)}")

def perform_game(cups: list, current_cup: int, count: int) -> None:
    for i in range(count):
        print(f"\nRound {i+1}")
        print(f"Cups : {', '.join([str(val) for val in cups[:10]])}")
        print(f"Current : {current_cup}")
        picked = pick_three(cups, current_cup)
        print(f"Picked : {picked}")
        destination = choose_destination(cups, current_cup, picked)
        print(f"Destination : {destination}")
        cups = create_new_circle(cups, picked, destination)
        current_cup = find_new_current(cups, current_cup)
    return cups

def pick_three(cups: list, current_cup: int) -> list:
    current_idx = cups.index(current_cup)
    if current_idx < len(cups) - 4:
        return cups[current_idx + 1:current_idx + 4]
    else:
        return cups[current_idx + 1:] + cups[:3 - (len(cups) - 1 - current_idx)]

def choose_destination(cups: list, current_cup: int, picked: list) -> str:
    destination = current_cup - 1
    while destination in picked or destination not in cups:
        destination -= 1
        if destination < 1:
            destination = len(cups)
    return destination

def create_new_circle(cups: list, picked: list, destination: int) -> list:
    new_cups = [destination]
    for val in picked:
        new_cups.append(val)
    destination_prev_idx = cups.index(destination)
    for val in cups[destination_prev_idx + 1:]:
        if val in picked:
            continue
        new_cups.append(val)
    for val in cups[:destination_prev_idx]:
        if val in picked:
            continue
        new_cups.append(val)
    return new_cups

def find_new_current(cups: list, current_cup: int) -> int:
    current_idx = cups.index(current_cup)
    if current_idx == len(cups) - 1:
        return cups[0]
    else:
        return cups[current_idx + 1]

def prepare_result_1(cups: list) -> str:
    result_list = []
    one_idx = cups.index(1)
    for val in cups[one_idx + 1:]:
        result_list.append(str(val))
    for val in cups[:one_idx]:
        result_list.append(str(val))
    return "".join(result_list)

def prepare_result_2(cups: list) -> int:
    one_idx = cups.index(1)
    return cups[one_idx + 1] * cups[one_idx + 2]

if __name__ == "__main__":
    print(run_script("input.txt"))