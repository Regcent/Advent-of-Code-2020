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
    seats_bin = raw_data.split("\n")
    seats = parse_seats(seats_bin)
    seats.sort()
    current = seats[0]
    for i in range(1, len(seats)):
        if seats[i] - current == 2:
            return current + 1
        else:
            current = seats[i]

def parse_seats(seats_bin: list) -> list:
    seats = []
    for seat_bin in seats_bin:
        row_bin = seat_bin[:7]
        col_bin = seat_bin[7:]
        seats.append(parse_row(row_bin) * 8 + parse_col(col_bin))
    return seats

def parse_row(row_bin: str) -> int:
    i = 0
    j = 127
    for char in row_bin:
        if char == "F":
            j = (i+j) // 2
        else:
            i = (i+j) // 2 + 1
    if i != j:
        print(f" ROW ISSUE i {i} j {j}")
    return i

def parse_col(col_bin: str) -> int:
    i = 0
    j = 7
    for char in col_bin:
        if char == "L":
            j = (i+j) // 2
        else:
            i = (i+j) // 2 + 1
    if i != j:
        print(f"COL ISSUE i {i} j {j}")
    return i

if __name__ == "__main__":
    print(run_script("input.txt"))