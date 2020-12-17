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
    return count_valid_passwords_in_file_normal(raw_data.split("\n"), True)

def is_sled_password_valid(target_char: str, min_count: int, max_count: int, password: str) -> bool:
    count = password.count(target_char)
    return 1 if min_count <= count and count <= max_count else 0

def is_toboggan_password_valid(target_char: str, first_pos: int, second_pos: int, password: str) -> bool:
    n = 0
    if password[first_pos - 1] == target_char:
        n += 1
    if password[second_pos - 1] == target_char:
        n += 1
    return n % 2

def count_valid_passwords_in_file_normal(pwds_to_check: list, sled: bool) -> int:
    total = 0
    for pwd_to_check in pwds_to_check:
        policy, password = pwd_to_check.split(":")
        password = password.strip()
        min_max, target_char = policy.split()
        min_count, max_count = [int(i) for i in min_max.split("-")]
        total += is_sled_password_valid(target_char, min_count, max_count, password) if sled else is_toboggan_password_valid(target_char, min_count, max_count, password)
    return total


if __name__ == "__main__":
    print(run_script("input_day2.txt"))