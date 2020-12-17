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
    lines = raw_data.split("\n")
    if lines[-1] != "":
        lines.append("")
    count = 0
    group = []
    for line in lines:
        if line == "":
            count += count_answers(group)
            group = []
        else:
            group.append(line)
    return count

def count_answers(group: list) -> int:
    answered = {}
    for answers in group:
        for question in answers:
            if question in answered:
                answered[question] += 1
            else:
                answered[question] = 1
    count = 0
    for q_id in answered:
        if answered[q_id] == len(group):
            count += 1
    return count

if __name__ == "__main__":
    print(run_script("input.txt"))