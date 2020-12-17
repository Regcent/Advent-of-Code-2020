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
    adapters = [int(i) for i in raw_data.split("\n")]
    adapters.sort()
    adapters = [0] + adapters
    adapters.append(adapters[len(adapters) - 1] + 3)
    #return count_diffs(adapters)
    sub_groups = find_sub_groups(adapters)
    total = 1
    for sub in sub_groups:
        if len(sub) < 3:
            continue
        elif len(sub) == 3:
            total *= 2
        elif len(sub) == 4:
            total *= 4
        elif len(sub) == 5:
            total *= 7
    return total
    
def find_sub_groups(adapters: list) -> list:
    sub_groups = [[0]]
    curr = adapters[0]
    for i in range(1, len(adapters)):
        if adapters[i] - curr == 3:
            sub_groups.append([adapters[i]])
        else:
            sub_groups[-1].append(adapters[i])
        curr = adapters[i]
    return sub_groups

def count_diffs(adapters: list) -> int:
    one_diff = 0
    three_diff = 0
    curr = adapters[0]
    for i in range(1, len(adapters)):
        if adapters[i] - curr == 1:
            one_diff += 1
        else:
            three_diff += 1
        curr = adapters[i]
    return one_diff * three_diff

if __name__ == "__main__":
    print(run_script("input.txt"))