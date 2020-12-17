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
    numbers = [int(i) for i in raw_data.split("\n")]
    invalid_number = 1504371145
    return find_xmas_weakness(numbers, invalid_number)

def find_xmas_weakness(numbers: list, target: int) -> int:
    total = numbers[0]
    start_idx = 0
    end_idx = 0
    i = 1
    while total != target:
        while total < target:
            total += numbers[i]
            end_idx += 1
            i += 1
        while total > target:
            total -= numbers[start_idx]
            start_idx += 1
    subset = numbers[start_idx:end_idx + 1]
    print(len(subset))
    return min(subset) + max(subset)


""" FIRST QUESTION
def find_xmas_weakness(numbers: list) -> int:
    for i in range(25, len(numbers)):
        current = numbers[i]
        if two_sum_in_list_extract(numbers, i-25, i, current):
            continue
        return current

def two_sum_in_list_extract(numbers: list, start: int, end: int, target: int) -> bool:
    candidates = []
    for i in range(start, end):
        candidates.append(numbers[i])
        if target - numbers[i] in candidates:
            return True
    return False
"""

if __name__ == "__main__":
    print(run_script("input.txt"))