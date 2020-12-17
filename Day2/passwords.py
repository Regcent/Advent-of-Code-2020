import time
import re

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

def count_valid_passwords_in_file_normal(filepath: str, sled: bool) -> int:
    start = time.time()
    total = 0
    with open(filepath, "r") as f:
        pwds_to_check = f.read().split("\n")
    for pwd_to_check in pwds_to_check:
        policy, password = pwd_to_check.split(":")
        password = password.strip()
        min_max, target_char = policy.split()
        min_count, max_count = [int(i) for i in min_max.split("-")]
        total += is_sled_password_valid(target_char, min_count, max_count, password) if sled else is_toboggan_password_valid(target_char, min_count, max_count, password)
    print(time.time() - start)
    return total

def count_valid_passwords_in_file_regex(filepath: str, sled: bool) -> int:
    start = time.time()
    total = 0
    pattern = re.compile(r"(\d+)-(\d+)\s+(\w)\:\s+(\w+)")
    with open(filepath, "r") as f:
        pwds_to_check = f.read().split("\n")
    for pwd_to_check in pwds_to_check:
        match = pattern.match(pwd_to_check)
        min_count = int(match.group(1))
        max_count = int(match.group(2))
        target_char = match.group(3)
        password = match.group(4)
        total += is_sled_password_valid(target_char, min_count, max_count, password) if sled else is_toboggan_password_valid(target_char, min_count, max_count, password)
    print(time.time() - start)
    return total