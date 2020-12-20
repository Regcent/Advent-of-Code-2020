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
    expressions = raw_data.split("\n")
    total = 0
    for expression in expressions:
        total += evaluate_1(expression)
    print(f"Answer 1 : {total}")
    total = 0
    for expression in expressions:
        val = evaluate_2(expression)
        total += val
    return f"Answer 2 : {total}"

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b



def remove_external_parentheses(expression: str) -> str:
    if not expression.startswith("("):
        return expression
    if expression.endswith(")"):
        opened_parentheses = 1
        for i in range(1, len(expression) - 1):
            if expression[i] == "(":
                opened_parentheses += 1
            elif expression[i] == ")":
                opened_parentheses -= 1
            else:
                continue
            if opened_parentheses == 0:
                return expression
        return expression[1:-1]
    return expression

def evaluate_1(expression: str) -> int:
    expression = expression.strip()
    expression = remove_external_parentheses(expression)
    if expression.isnumeric():
        return int(expression)
    opened_parentheses = 0
    for i in range(len(expression)-1, -1, -1):
        if expression[i] == "(":
            opened_parentheses -= 1
        elif expression[i] == ")":
            opened_parentheses += 1
        elif expression[i] == "+":
            if opened_parentheses == 0:
                return add(evaluate_1(expression[:i]), evaluate_1(expression[i+1:]))
        elif expression[i] == "*":
            if opened_parentheses == 0:
                return multiply(evaluate_1(expression[:i]), evaluate_1(expression[i+1:]))

def evaluate_2(expression: str) -> int:
    expression = expression.strip()
    expression = remove_external_parentheses(expression)
    if expression.isnumeric():
        return int(expression)
    opened_parentheses = 0
    for i in range(len(expression)-1, -1, -1):
        if expression[i] == "(":
            opened_parentheses -= 1
        elif expression[i] == ")":
            opened_parentheses += 1
        elif expression[i] == "*":
            if opened_parentheses == 0:
                return multiply(evaluate_2(expression[:i]), evaluate_2(expression[i+1:]))
        else:
            continue
    opened_parentheses = 0
    for i in range(len(expression)-1, -1, -1):
        if expression[i] == "(":
            opened_parentheses -= 1
        elif expression[i] == ")":
            opened_parentheses += 1
        elif expression[i] == "+":
            if opened_parentheses == 0:
                return add(evaluate_2(expression[:i]), evaluate_2(expression[i+1:]))
        else:
            continue


if __name__ == "__main__":
    print(run_script("input.txt"))