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
    starting_numbers = [int(i) for i in raw_data.split(",")]
    spoken_numbers = []
    numbers_dict = {}
    for i in range(len(starting_numbers)):
        spoken_numbers.append(starting_numbers[i])
        if i != len(starting_numbers) - 1:
            numbers_dict[starting_numbers[i]] = i
    for j in range(i, 30000000):
        last_spoken = spoken_numbers[-1]
        if last_spoken not in numbers_dict:
            spoken_numbers.append(0)
        else:
            spoken_numbers.append(j - numbers_dict[last_spoken])
        numbers_dict[last_spoken] = j
    return spoken_numbers[:10], spoken_numbers[30000000 - 1]

if __name__ == "__main__":
    print(run_script("input.txt"))