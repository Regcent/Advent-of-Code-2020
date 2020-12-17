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
    bag_dict = parse_bags(lines)
    return count_contained_bags(bag_dict, "shiny gold")
    
def count_container_bags(lines: list, color: str) -> int:
    count = 0
    checked = 0
    bag_colors = [color]
    while checked < len(bag_colors):
        current_color = bag_colors[checked]
        for line in lines:
            container, colors = line.split("contain")
            if current_color not in colors:
                continue
            container = container[:-6]
            if container in bag_colors:
                continue
            bag_colors.append(container)
        checked += 1
        print(len(bag_colors), checked)
    return len(bag_colors) - 1


def count_contained_bags_old(lines: list, color: str) -> int:
    count = 1
    target_line = ""
    for line in lines:
        container, colors = line.split("contain")
        if color not in container:
            continue
        if "no other bags" in colors:
            return 1
        bags = colors.split(",")
        print(bags)
        for bag in bags:
            bag = bag.strip()
            bag_count = int(bag[0])
            if bag_count == 1:
                color = bag[2:-4]
            else:
                color = bag[2:-5]
            color = color.strip()
            print(bag_count, color)
            contained_bags = count_contained_bags(lines, color)
            count += bag_count * contained_bags
            print(count)
        return count

def count_contained_bags(bag_dict: dict, color: str) -> int:
    count = 1
    if not bag_dict[color]:
        return count
    for bag_color in bag_dict[color]:
        count += bag_dict[color][bag_color] * count_contained_bags(bag_dict, bag_color)
    return count

def parse_bags(lines: list) -> dict:
    bag_dict = {}
    for line in lines:
        container, colors = line.split(" bags contain ")
        #container = container.replace(" bags", "").strip()
        bag_dict[container] = {}
        if "no other bags" in colors:
            continue
        bags = colors.split(", ")
        for bag in bags:
            bag_count = int(bag[0])
            if bag_count == 1:
                color = bag[2:-4]
            else:
                color = bag[2:-5]
            color = color.strip()
            bag_dict[container][color] = bag_count
    return bag_dict

if __name__ == "__main__":
    print(run_script("input.txt"))