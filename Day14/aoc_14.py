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
    return run_init(lines)
    
def run_init(lines: list) -> int:
    mem = {}
    mask = 0
    for line in lines:
        order, value = line.split(" = ")
        if "mask" in order:
            mask = calculate_mask(value)
        else:
            index = order.split("[")[1][:-1]
            value = int(value)
            write_value_in_memory_2(mem, index, value, mask)
    total = 0
    for index in mem:
        total += mem[index]
    return total

def calculate_mask(value: str) -> dict:
    mask = {}
    offset = len(value) - 1
    for i in range(len(value)):
        mask[offset - i] = value[i]
    return mask

def write_value_in_memory_1(mem: dict, index: int, value: int, mask: dict) -> None:
    for bit in mask:
        if mask[bit] == "X":
            continue
        is_bit_set_in_value = bool(value & (2 ** int(bit)))
        if is_bit_set_in_value and mask[bit] == "0":
            value -= 2 ** int(bit)
        elif not is_bit_set_in_value and mask[bit] == "1":
            value += 2 ** int(bit)
    mem[index] = value

def write_value_in_memory_2(mem: dict, initial_index: str, value: int, mask: dict) -> None:
    index_list = [int(initial_index)]
    for bit in mask:
        if mask[bit] == "0":
            continue
        elif mask[bit] == "1":
            bit_val = 2 ** int(bit)
            for i in range(len(index_list)):
                if not index_list[i] & bit_val:
                    index_list[i] += bit_val
        else:
            bit_val = 2 ** int(bit)
            new_indexes = []
            for index in index_list:
                is_bit_set_in_index = bool(index & bit_val)
                if is_bit_set_in_index:
                    new_indexes.append(index - bit_val)
                else:
                    new_indexes.append(index + bit_val)
            for index in new_indexes:
                index_list.append(index)
    for index in index_list:
        mem[index] = value


if __name__ == "__main__":
    print(run_script("input.txt"))