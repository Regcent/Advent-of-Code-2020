import time
from typing import Union

class Cube:

    def __init__(self, length: int, width: int, height: int):
        self.length = length
        self.width = width
        self.height = height
        self.layers = [Layer(length, width) for i in range(height)]
        self.active_count = 0

    def set_active(self, x: int, y: int, z: int) -> None:
        self.layers[z].rows[y].cells[x].active = True
        self.active_count += 1

    def neighbors(self, x: int, y: int, z: int) -> list:
        neighbors = []
        for z_c in range(z - 1 if z > 0 else z, z + 2 if z < self.height - 1 else z + 1):
            for y_c in range(y - 1 if y > 0 else y, y + 2 if y < self.width - 1 else y + 1):
                for x_c in range(x - 1 if x > 0 else x, x + 2 if x < self.length - 1 else x + 1):
                    if x_c == x and y_c == y and z_c == z:
                        continue
                    neighbors.append(self.layers[z_c].rows[y_c].cells[x_c])
        return neighbors

    def count_active_neighbors(self, x: int, y: int, z: int) -> int:
        active = 0
        for neighbor in self.neighbors(x, y, z):
            if neighbor.active == True:
                active += 1
        return active

    def cube_cycle(self):
        new_cube = Cube(self.length + 2, self.width + 2, self.height + 2)
        for z in range(self.height):
            for y in range(self.width):
                for x in range(self.length):
                    if self.layers[z].rows[y].cells[x].active:
                        active_neighbors = self.count_active_neighbors(x, y, z)
                        if 2 == active_neighbors or active_neighbors == 3:
                            new_cube.set_active(x + 1, y + 1, z + 1)
                    else:
                        if self.count_active_neighbors(x, y, z) == 3:
                            new_cube.set_active(x + 1, y + 1, z + 1)
        return new_cube

    def __str__(self) -> str:
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
        self.cells = [Cell() for i in range(length)]

    def __str__(self):
        return "".join([str(cell) for cell in self.cells])

class Cell:

    def __init__(self):
        self.active = False

    def __str__(self):
        return "#" if self.active else "."

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
    cube = Cube(len(data[0]) + 2, len(data) + 2, 5)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "#":
                cube.set_active(j + 1, i + 1, 2)
    for i in range(6):
        cube = cube.cube_cycle()
    return cube.active_count

if __name__ == "__main__":
    print(run_script("input.txt"))