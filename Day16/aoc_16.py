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
    rules = {}
    own_ticket = []
    other_tickets = []
    parse_input(lines, rules, own_ticket, other_tickets)

    ### PART 2
    valid_tickets = []
    invalid_tickets = 0
    total_invalid = 0
    for ticket in other_tickets:
        if ticket_scanning_error_rate(ticket, rules) == 0 and ticket[13] != 0: # Dirty fix : 0 is an invalid value, but error rate is the sum of invalid values... and error rate is then 0
            valid_tickets.append(ticket)
        else:
            invalid_tickets += 1
            total_invalid += ticket_scanning_error_rate(ticket, rules)
    rules_idx = {}
    for i in range(len(own_ticket)):
        rules_idx[i] = list(rules.keys())
    for ticket in valid_tickets:
        guess_rules(rules, ticket, rules_idx)
    found_singletons = []
    while True :
        new_singleton = -1
        field_name = ""
        for i in range(len(own_ticket)):
            if i in found_singletons:
                continue
            if len(rules_idx[i]) == 1:
                new_singleton = i
                field_name = rules_idx[i][0]
                break
        if new_singleton == -1:
            break
        for i in range(len(own_ticket)):
            if i == new_singleton:
                continue
            if field_name in rules_idx[i]:
                rules_idx[i].remove(field_name)
        found_singletons.append(new_singleton)
    
    product = 1
    for i in range(len(own_ticket)):
        if "departure" in rules_idx[i][0]:
            product *= own_ticket[i]
    return product
    """ PART 1
    total_error_rate = 0
    for ticket in other_tickets:
        total_error_rate += ticket_scanning_error_rate(ticket, rules)
    return total_error_rate
    """

def parse_input(lines: list, rules: dict, own_ticket: list, other_tickets: list) -> None:
    idx = 0
    while lines[idx] != "":
        rule_name, values = lines[idx].split(": ")
        interval_1, interval_2 = values.split(" or ")
        rules[rule_name] = []
        rules[rule_name].append(tuple(int(i) for i in interval_1.split("-")))
        rules[rule_name].append(tuple(int(i) for i in interval_2.split("-")))
        idx += 1
    idx += 1
    while lines[idx] != "":
        if "your" in lines[idx]:
            idx += 1
            continue
        for value in lines[idx].split(","):
            own_ticket.append(int(value))
        idx += 1
    idx += 1
    while lines[idx] != "":
        if "nearby" in lines[idx]:
            idx += 1
            continue
        other_tickets.append([int(i) for i in lines[idx].split(",")])
        idx += 1

def ticket_scanning_error_rate(ticket: list, rules: dict) -> int:
    error_rate = 0
    for value in ticket:
        field_found = False
        for field in rules:
            for interval in rules[field]:
                if interval[0] <= value <= interval[1]:
                    field_found = True
                    break
        if not field_found:
            error_rate += value
    return error_rate

def guess_rules(rules: dict, ticket: list, rules_idx: dict) -> None:
    for i in range(len(ticket)):
        value = ticket[i]
        for field in rules:
            possible_field = False
            for interval in rules[field]:
                if interval[0] <= value <= interval[1]:
                    possible_field = True
            if not possible_field:
                if i == 13:
                    print(ticket, field, ticket[13])
                if field in rules_idx[i]:
                    rules_idx[i].remove(field)

if __name__ == "__main__":
    print(run_script("input.txt"))