import time
from typing import Union

class Seat:

    def __init__(self, is_floor, is_free, is_occupied, neighbors):
        self.is_floor = is_floor
        self.is_free = is_free
        self.is_occupied = is_occupied
        self.neighbors = neighbors

    def __eq__(self, other):
        return self.is_floor == other.is_floor and self.is_free == other.is_free and self.is_occupied == other.is_occupied

class Map:

    def __init__(self):
        self.map = []
        self.current_row = -1
        self.occupied_count = 0
        self.seat_count = 0
        self.width = 99
        self.height = 90

    def __eq__(self, other):
        for i in range(self.height):
            for j in range(self.width):
                if self.map[i][j] == other.map[i][j]:
                    continue
                return False
        return True

    def new_row(self):
        self.map.append([])
        self.current_row += 1
    
    def new_seat(self, is_floor, is_free, is_occupied, neighbors):
        self.map[self.current_row].append(Seat(is_floor, is_free, is_occupied, neighbors))
        self.seat_count += 1
        if is_occupied:
            self.occupied_count += 1

    def create_new_map_1(self):
        new_map = Map()
        for i in range(self.height):
            new_map.new_row()
            for j in range(self.width):
                seat = self.map[i][j]
                if seat.is_floor:
                    new_map.new_seat(True, False, False, seat.neighbors)
                    continue
                occupied = 0
                for (row, col) in seat.neighbors:
                    if self.map[row][col].is_occupied:
                        occupied += 1
                if seat.is_free and occupied == 0:
                    new_map.new_seat(False, False, True, seat.neighbors)
                elif seat.is_occupied and occupied >= 4:
                    new_map.new_seat(False, True, False, seat.neighbors)
                else:
                    new_map.new_seat(False, seat.is_free, seat.is_occupied, seat.neighbors)
        return new_map

    def create_new_map_2(self):
        new_map = Map()
        for i in range(self.height):
            new_map.new_row()
            for j in range(self.width):
                seat = self.map[i][j]
                if seat.is_floor:
                    new_map.new_seat(True, False, False, seat.neighbors)
                    continue
                occupied = 0
                for (row, col) in seat.neighbors:
                    if self.map[row][col].is_occupied:
                        occupied += 1
                if seat.is_free and occupied == 0:
                    new_map.new_seat(False, False, True, seat.neighbors)
                elif seat.is_occupied and occupied >= 5:
                    new_map.new_seat(False, True, False, seat.neighbors)
                else:
                    new_map.new_seat(False, seat.is_free, seat.is_occupied, seat.neighbors)
        return new_map

    def find_neighbors_1(self, row, col):
        if row == 0 and col == 0:
            neighbors = [(row, col+1), (row+1, col), (row+1, col+1)]
        elif row == 0 and col == self.width - 1:
            neighbors = [(row, col-1), (row+1, col-1), (row+1, col)]
        elif row == self.height - 1 and col == 0:
           neighbors = [(row-1, col), (row-1, col+1), (row, col+1)]
        elif row == self.height - 1 and col == self.width - 1:
             neighbors = [(row-1, col-1), (row-1, col), (row, col-1)]
        elif row == 0:
            neighbors = [(row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]
        elif row == self.height - 1:
            neighbors = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1)]
        elif col == 0:
            neighbors = [(row-1, col), (row-1, col+1), (row, col+1), (row+1, col), (row+1, col+1)]
        elif col == self.width - 1:
            neighbors = [(row-1, col-1), (row-1, col), (row, col-1), (row+1, col-1), (row+1, col)]
        else:
            neighbors = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]
        return neighbors

    def find_neighbors_2(self, row, col):
        neighbors = []
        #TOP
        for i in range(row-1, -1, -1):
            if not self.map[i][col].is_floor:
                neighbors.append((i, col))
                break
        #LEFT
        for j in range(col-1, -1, -1):
            if not self.map[row][j].is_floor:
                neighbors.append((row, j))
                break
        #RIGHT&
        for j in range(col+1, self.width, 1):
            if not self.map[row][j].is_floor:
                neighbors.append((row, j))
                break
        #BOT
        for i in range(row+1, self.height, 1):
            if not self.map[i][col].is_floor:
                neighbors.append((i, col))
                break
        #TOPLEFT
        i = 1
        while True:
            if row - i < 0:
                break
            if col - i < 0:
                break
            if not self.map[row-i][col-i].is_floor:
                neighbors.append((row-i, col-i))
                break
            i += 1
        #TOPRIGHT
        i = 1
        while True:
            if row - i < 0:
                break
            if col + i >= self.width:
                break
            if not self.map[row-i][col+i].is_floor:
                neighbors.append((row-i, col+i))
                break
            i += 1
        #BOTLEFT
        i = 1
        while True:
            if row + i >= self.height:
                break
            if col - i < 0:
                break
            if not self.map[row+i][col-i].is_floor:
                neighbors.append((row+i, col-i))
                break
            i += 1
        #BOTRIGHT
        i = 1
        while True:
            if row + i >= self.height:
                break
            if col + i >= self.width:
                break
            if not self.map[row+i][col+i].is_floor:
                neighbors.append((row+i, col+i))
                break
            i += 1
        return neighbors

    def define_neighbors_1(self):
        for i in range(self.height):
            for j in range(self.width):
                seat = self.map[i][j]
                if seat.is_floor:
                    continue
                for coord in self.find_neighbors_1(i,j):
                    seat.neighbors.append(coord)

    def define_neighbors_2(self):
        for i in range(self.height):
            for j in range(self.width):
                seat = self.map[i][j]
                if seat.is_floor:
                    continue
                for coord in self.find_neighbors_2(i,j):
                    seat.neighbors.append(coord)

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
    seats = create_map(raw_data)
    seats.define_neighbors_2()
    print(seats.map[0][0].neighbors)
    return find_stable(seats).occupied_count

def create_map(raw_data: str) -> Map:
    rows = raw_data.split("\n")
    seats = Map()
    for row in rows:
        seats.new_row()
        for char in row:
            if char == ".":
                seats.new_seat(True, False, False, [])
            else:
                seats.new_seat(False, True, False, [])
    return seats

def find_stable(seats: Map) -> int:
    count = 1
    old_map = seats
    new_map = seats.create_new_map_2()
    while old_map != new_map:
        print(count)
        old_map = new_map
        new_map = new_map.create_new_map_2()
        count += 1
    return new_map

if __name__ == "__main__":
    print(run_script("input.txt"))