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
    card_sbj_num = 7
    door_sbj_num = 7
    divider = 20201227
    card_pub_key, door_pub_key = [int(i) for i in raw_data.split("\n")]
    card_loop_sz = calculate_loop_size(card_sbj_num, divider, card_pub_key)
    door_loop_sz = calculate_loop_size(door_sbj_num, divider, door_pub_key)
    if card_loop_sz < door_loop_sz:
        print(f"Result Part 1 : {calculate_secret_key(door_pub_key, card_loop_sz, divider)}")
    else:
        print(f"Result Part 2 : {calculate_secret_key(card_pub_key, door_loop_sz, divider)}")

def calculate_loop_size(sbj_num: int, divider: int, pub_key: int) -> int:
    sbj_num_looped = [1]
    current_loop_val = 1
    while current_loop_val != pub_key:
        current_loop_val = (current_loop_val * sbj_num) % divider
        sbj_num_looped.append(current_loop_val)
    return len(sbj_num_looped) - 1

def calculate_secret_key(sbj_num: int, loop_sz: int, divider: int) -> int:
    total = 1
    for i in range(loop_sz):
        total = (total * sbj_num) % divider
    return total

if __name__ == "__main__":
    print(run_script("input.txt"))