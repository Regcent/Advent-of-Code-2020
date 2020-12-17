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
    estimated_arrival = int(lines[0])
    buses = []
    for bus_id in lines[1].split(","):
        if bus_id == "x":
            buses.append(-1)
            continue
        buses.append(int(bus_id))
    print(estimated_arrival, buses)    
    return find_optimal_timeslot(buses)

def find_optimal_timeslot(buses:list):
    offsets = {}
    for i in range(len(buses)):
        if buses[i] == -1:
            continue
        offsets[buses[i]] = i
    print(offsets)
    buses_ids = list(offsets.keys())
    print(buses_ids)
    candidate = buses_ids[0]
    step = buses_ids[0]
    for bus_id in buses_ids[1:]:
        remainder = (candidate + offsets[bus_id]) % bus_id
        while remainder != 0:
            candidate += step
            remainder = (candidate + offsets[bus_id]) % bus_id
            print(remainder)
        step *= bus_id
        print(candidate)
    return candidate


def find_first_bus(estimated: int, buses: list) -> int:
    min_reminder = max(buses)
    current_candidate = -1
    for bus in buses:
        if bus == -1:
            continue
        reminder = estimated % bus
        if reminder == 0:
            min_reminder = 0
            current_candidate = bus
        else:
            reminder = bus - reminder
            if reminder < min_reminder:
                min_reminder = reminder
                current_candidate = bus
    print(current_candidate * min_reminder)
    return current_candidate

if __name__ == "__main__":
    print(run_script("input.txt"))