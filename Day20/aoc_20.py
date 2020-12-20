import time
from typing import Union


class Tile:

    

    def __init__(self, tile_id: int, data: list):
        self.tile_id = tile_id
        self.data = []
        self.width = 10
        for i in range(len(data)):
            self.data.append([])
            for j in range(len(data[i])):
                self.data[i].append(data[i][j])
        self.hashes = {}
        self.matches = {}
        ### LEFT
        hash_val_1 = 0
        hash_val_2 = 0
        for i in range(len(data)):
            if data[i][0] == "#":
                hash_val_1 += 2 ** i
                hash_val_2 += 2 ** (self.width - 1 - i)
        self.hashes["left"] = [hash_val_1, hash_val_2]
        ### RIGHT
        hash_val_1 = 0
        hash_val_2 = 0
        for i in range(len(data)):
            if data[i][9] == "#":
                hash_val_1 += 2 ** i
                hash_val_2 += 2 ** (self.width - 1 - i)
        self.hashes["right"] = [hash_val_1, hash_val_2]
        ### TOP
        hash_val_1 = 0
        hash_val_2 = 0
        for i in range(len(data)):
            if data[0][i] == "#":
                hash_val_1 += 2 ** i
                hash_val_2 += 2 ** (self.width - 1 - i)
        self.hashes["top"] = [hash_val_1, hash_val_2]
        ### BOT
        hash_val_1 = 0
        hash_val_2 = 0
        for i in range(len(data)):
            if data[9][i] == "#":
                hash_val_1 += 2 ** i
                hash_val_2 += 2 ** (self.width - 1 - i)
        self.hashes["bot"] = [hash_val_1, hash_val_2]


    def __str__(self):
        lines = [f"Tile {self.tile_id}:"]
        for i in range(len(self.data)):
            lines.append("".join([self.data[i][j] for j in range(len(self.data[i]))]))
        return "\n".join(lines)
        

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
    tiles = []
    parse_tiles(raw_data.split("\n\n"), tiles)
    match_tiles(tiles)
    two_match = []
    for i in range(len(tiles)):
        if len(list(tiles[i].matches.keys())) == 2:
            two_match.append(tiles[i].tile_id)
    print(f"Corners : {', '.join([str(i) for i in two_match])}")
    result = 1
    for val in two_match:
        result *= val
    print(f"Part 1 result: {result}")

def parse_tiles(raw_tiles: list, tiles: list) -> None:
    for raw_tile in raw_tiles:
        lines = raw_tile.split("\n")
        tile_id = int(lines[0].split(" ")[1][:-1])
        tiles.append(Tile(tile_id, lines[1:]))

def match_tiles(tiles: list) -> None:
    for i in range(len(tiles) - 1):
        for j in range(i + 1, len(tiles)):
            for target_side in tiles[i].hashes:
                if target_side in tiles[i].matches:
                    continue
                hash_target = tiles[i].hashes[target_side][0]
                match_found = False
                if match_found:
                    break
                for test_side in tiles[j].hashes:
                    if test_side in tiles[j].matches:
                        continue
                    if match_found:
                        break
                    for val in tiles[j].hashes[test_side]:
                        if hash_target == val:
                            match_found = True
                            tiles[i].matches[target_side] = tiles[j].tile_id
                            tiles[j].matches[test_side] = tiles[i].tile_id

if __name__ == "__main__":
    print(run_script("input.txt"))