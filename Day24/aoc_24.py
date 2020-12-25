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
    flipped_tiles = parse_flipped_tiles(raw_data.split("\n"))
    print(f"Result Part 1 : {len(flipped_tiles)}")
    tiles = {}
    for tile in flipped_tiles:
        tiles[tile] = {}
        tiles[tile]["black"] = True
        tiles[tile]["neighbors"] = get_neighbors(tile)
        for neighbor in tiles[tile]["neighbors"]:
            if neighbor in tiles:
                continue
            tiles[neighbor] = {}
            tiles[neighbor]["black"] = False
            tiles[neighbor]["neighbors"] = get_neighbors(neighbor)
    for i in range(100):
        tiles = new_flip(tiles)
    total = 0
    black = []
    for tile in tiles:
        if tiles[tile]["black"]:
            total += 1
            black.append(tile)
    print(f"Result Part 2 : {total}")

def new_flip(tiles: dict) -> dict:
    new_flip = {}
    for tile in tiles:
        new_flip[tile] = {}
        new_flip[tile]["neighbors"] = tiles[tile]["neighbors"]
    for tile in tiles:
        black_count = get_black_count(tiles, tile)
        if tiles[tile]["black"]:
            if black_count == 0 or black_count > 2:
                new_flip[tile]["black"] = False
            else:
                new_flip[tile]["black"] = True
        else:
            if black_count == 2:
                new_flip[tile]["black"] = True
                for neighbor in tiles[tile]["neighbors"]:
                    if neighbor not in new_flip:
                        new_flip[neighbor] = {}
                        new_flip[neighbor]["black"] = False
                        new_flip[neighbor]["neighbors"] = get_neighbors(neighbor)
            else:
                new_flip[tile]["black"] = False
    return new_flip

def get_black_count(tiles: dict, tile: tuple) -> int:
    count = 0
    for neighbor in tiles[tile]["neighbors"]:
        if neighbor not in tiles:
            continue
        if tiles[neighbor]["black"]:
            count += 1
    return count 

def get_neighbors(tile: tuple) -> list:
    w = tile[0]
    ne = tile[1]
    return [(w - 1, ne), (w - 1, ne - 1), (w, ne - 1), (w + 1, ne), (w + 1, ne + 1), (w, ne + 1)]


def parse_flipped_tiles(lines: list) -> list:
    flipped_tiles = []
    for line in lines:
        west = 0
        northeast = 0
        i = 0
        while i < len(line):
            if line[i] == "e":
                west -= 1
                i += 1
            elif line[i] == "w":
                west += 1
                i += 1
            elif line[i] == "n":
                if line[i + 1] == "e":
                    northeast += 1
                elif line[i + 1] == "w":
                    northeast += 1
                    west += 1
                i += 2
            elif line[i] == "s":
                if line[i + 1] == "e":
                    northeast -= 1
                    west -=1
                elif line[i + 1] == "w":
                    northeast -= 1
                i += 2
        if (west, northeast) in flipped_tiles:
            flipped_tiles.remove((west, northeast))
        else:
            flipped_tiles.append((west, northeast))
    return flipped_tiles

if __name__ == "__main__":
    print(run_script("input.txt"))