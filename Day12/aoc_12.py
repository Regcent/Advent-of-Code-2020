import time
from typing import Union
from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Position:

    def __init__(self):
        self.direction = Direction.EAST
        self.vertical = 0
        self.horizontal = 0

    def define_waypoint(self):
        self.waypoint = Position()
        self.waypoint.vertical = 1
        self.waypoint.horizontal = 10

    def move_1(self, direction: Direction, count: int):
        if direction == Direction.NORTH:
            self.vertical += count
        elif direction == Direction.SOUTH:
            self.vertical -= count
        elif direction == Direction.EAST:
            self.horizontal += count
        elif direction == Direction.WEST:
            self.horizontal -= count
        else:
            print(f"Wrong direction : {direction}")

    def turn_1(self, axis: str, angle: int):
        initial_direction = self.direction.value
        if axis == "R":
            new_direction = initial_direction + angle // 90
        elif axis == "L":
            new_direction = initial_direction - angle // 90
        else:
            print(f"Wrong axis: {axis}")
        self.direction = Direction(new_direction % 4)
    
    def forward_1(self, count: int):
        self.move_1(self.direction, count)

    def move_2(self, direction: Direction, count: int):
        if direction == Direction.NORTH:
            self.waypoint.vertical += count
        elif direction == Direction.SOUTH:
            self.waypoint.vertical -= count
        elif direction == Direction.EAST:
            self.waypoint.horizontal += count
        elif direction == Direction.WEST:
            self.waypoint.horizontal -= count
        else:
            print(f"Wrong direction : {direction}")

    def turn_2(self, axis: str, angle: int):
        if axis == "L":
            while angle > 0:
                horizontal = self.waypoint.horizontal
                vertical = self.waypoint.vertical
                self.waypoint.vertical = horizontal
                self.waypoint.horizontal = -vertical
                angle -= 90
        elif axis == "R":
            while angle > 0:
                horizontal = self.waypoint.horizontal
                vertical = self.waypoint.vertical
                self.waypoint.vertical = -horizontal
                self.waypoint.horizontal = vertical
                angle -= 90

    def forward_2(self, count: int):
        self.vertical += count * self.waypoint.vertical
        self.horizontal += count * self.waypoint.horizontal

    def __str__(self):
        return f"Direction : {self.direction}, Vertical: {self.vertical}, horizontal: {self.horizontal}"

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
    directions = raw_data.split("\n")
    final_position = calculate_directions(directions)
    return abs(final_position.horizontal) + abs(final_position.vertical)

def calculate_directions(directions: list) -> Position:
    position = Position()
    position.define_waypoint()
    for dir in directions:
        order = dir[0]
        count = int(dir[1:])
        if order == "N":
            position.move_2(Direction.NORTH, count)
        elif order =="W":
            position.move_2(Direction.WEST, count)
        elif order == "S":
            position.move_2(Direction.SOUTH, count)
        elif order == "E":
            position.move_2(Direction.EAST, count)
        elif order == "F":
            position.forward_2(count)
        elif order == "L":
            position.turn_2(order, count)
        elif order == "R":
            position.turn_2(order, count)
        else:
            print(f"Invalid order: {order}")
        """print(dir)
        print(position)
        print(f"Waypoint : {position.waypoint}")
        """
    return position
        
if __name__ == "__main__":
    print(run_script("input.txt"))