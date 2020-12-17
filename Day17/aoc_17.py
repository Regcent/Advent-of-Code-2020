import time
from typing import Union

class Cube:

    def __init__(self, length: int, width: int, height: int):
        self.length = length
        self.width = width
        self.height = height
        self.layers = [Layer(length, width) for i in range(height)]

    def set_active(self, x: int, y: int, z: int):
        self.layers[z].rows[y].cells[x] = True

    def __str__(self):
        return "\n\n".join([f"z={z}\n{str(self.layers[z])}" for z in range(self.height)])

class Layer:
    
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self.rows = [Row(length) for i in range(width)]

    def __str__(self):
        return "\n".join([str(row) for row in self.rows])

class Row:

    def __init__(self, length: int):
        self.cells = [False for i in range(length)]

    def __str__(self):
        return "".join(["#" if cell else "." for cell in self.cells])

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
    data = raw_data.split("\n")
    cube_init = Cube(len(data[0]), len(data), 3)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "#":
                cube_init.set_active(j, i, 1)
    print(cube_init)


if __name__ == "__main__":
    print(run_script("input.txt"))