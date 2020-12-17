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
    rows = raw_data.split("\n")
    hits = []
    hits.append(check_slope(rows, 1, 1))
    hits.append(check_slope(rows, 3, 1))
    hits.append(check_slope(rows, 5, 1))
    hits.append(check_slope(rows, 7, 1))
    hits.append(check_slope(rows, 1, 2))
    print(hits)
    total = 1
    for hit_count in hits:
        total *= hit_count
    return total

def check_slope(rows: list, d_x: int, d_y: int) -> int:
    current_row = 0
    current_col = 0
    row_size = len(rows[0])
    count = 0
    while current_row < len(rows) - 1:
        current_row += d_y
        current_col += d_x
        if current_col >= row_size:
            current_col -= row_size
        if rows[current_row][current_col] == "#":
            count += 1
    return count

def check_slope_modulo(rows: list, d_x: int, d_y: int) -> int:
    current_row = 0
    current_col = 0
    row_size = len(rows[0])
    count = 0
    while current_row < len(rows) - 1:
        current_row += d_y
        current_col += d_x
        current_col = current_col % row_size
        if rows[current_row][current_col] == "#":
            count += 1
    return count

if __name__ == "__main__":
    print(run_script("input_day3.txt"))