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
    return count_valid_passports(lines)

def count_valid_passports(lines: list) -> int:
    mandatory = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional = ["cid"]
    passport = {}
    count = 0
    if lines[-1] != "":
        lines.append("")
    for line in lines:
        if line == "":
            if is_passport_valid(passport, mandatory, optional):
                count += 1
            else:
                print(f"{passport}")
            passport = {}
        else:
            fields = line.split(" ")
            for field in fields:
                key, data = field.split(":")
                passport[key] = data
    return count

def is_passport_valid(passport: dict, mandatory: list, optional: list) -> bool:
    if not check_passport_keys(passport, mandatory, optional):
        return False
    if not check_year(passport, "byr", 1920, 2002):
        return False
    if not check_year(passport, "iyr", 2010, 2020):
        return False
    if not check_year(passport, "eyr", 2020, 2030):
        return False
    if not check_height(passport):
        return False
    if not check_hair_color(passport):
        return False
    if not check_eye_color(passport):
        return False
    if not check_pid(passport):
        return False
    return True

def check_hair_color(passport: dict) -> bool:
    hcl = passport["hcl"]
    if hcl[0] != "#":
        return False
    hcl = hcl[1:]
    valid_chars = "0123456789abcdef"
    for char in hcl:
        if char not in valid_chars:
            return False
    return True

def check_eye_color(passport: dict) -> bool:
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    ecl = passport["ecl"]
    return ecl in valid

def check_pid(passport: dict) -> bool:
    pid = passport["pid"]
    if len(pid) != 9:
        return False
    try:
        pid = int(pid)
        return True
    except:
        return False

def check_height(passport:dict) -> bool:
    height = passport["hgt"]
    unit = height[-2:]
    value = height[:-2]
    try:
        value = int(value)
    except:
        return False
    if unit == "in":
        return value >= 59 and value <= 76
    elif unit == "cm":
        return value >= 150 and value <= 193
    else:
        return False

def check_year(passport: dict, key: str, min_val: int, max_val: int) -> bool:    
    val = passport[key]
    try:
        val = int(val)
        return val >= min_val and val <= max_val
    except:
        return False

def check_passport_keys(passport: dict, mandatory: list, optional: list) -> bool:
    for key in mandatory:
        try:
            test = passport[key]
        except:
            return False
    return True

if __name__ == "__main__":
    print(run_script("input_day4.txt"))