import time
from typing import Union

class MutableIndex:

    def __init__(self):
        self.index = 0
        
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
        total += evaluate_expression(expression, MutableIndex())
    print(f"Answer 1 : {total}")
    total = 0
    for expression in expressions:
        adapted = "".join(adapt_expression(expression, MutableIndex()))
        print(adapted)
        total += evaluate_expression(adapted, MutableIndex())
    return f"Answer 2 : {total}"

def adapt_expression(expression: str, m: MutableIndex) -> list:
    components = []
    prepare_closing = False
    while m.index < len(expression):
        if expression[m.index] == " ":
            m.index += 1
            continue
        elif expression[m.index] == "(":
            components.append(expression[m.index])
            m.index += 1
            for comp in adapt_expression(expression, m):
                components.append(comp)
            if prepare_closing:
                components.append(")")
                prepare_closing = False
        elif expression[m.index] == ")":
            components.append(expression[m.index])
            m.index += 1
            return components
        elif expression[m.index] == "+":
            parentheses = 0
            for i in range(len(components) - 1, -1, -1):
                if components[i] == ")":
                    parentheses += 1
                elif components[i] == "(":
                    parentheses -= 1
                elif components[i] == "*" or components[i] == "+":
                    continue
                else:
                    if parentheses == 0:
                        components.insert(i , "(")
                        break
            components.append(expression[m.index])
            m.index += 1
            prepare_closing = True
        else:
            components.append(expression[m.index])
            m.index += 1
            if prepare_closing:
                components.append(")")
                prepare_closing = False
    return components

def evaluate(a: int, b: int, operation: str) -> int:
    if operation == "+":
        return a + b
    elif operation == "*":
        return a * b
    else:
        return a + b

def evaluate_expression(expression: str, m: MutableIndex) -> int:
    value = 0
    prepare_operation = ""
    while m.index < len(expression):
        if expression[m.index] == "(":
            m.index += 1
            value = evaluate(value, evaluate_expression(expression, m), prepare_operation)
        elif expression[m.index] == ")":
            m.index += 1
            return value
        elif expression[m.index] == " ":
            m.index += 1
            continue
        elif expression[m.index] == "+" or expression[m.index] == "*":
            prepare_operation = expression[m.index]
            m.index += 1
        else:
            if prepare_operation == "":
                value += int(expression[m.index])
            else:
                value = evaluate(value, int(expression[m.index]), prepare_operation)
                prepare_operation = ""
            m.index += 1
    return value


if __name__ == "__main__":
    print(run_script("example.txt"))