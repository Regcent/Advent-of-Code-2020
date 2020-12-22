import time
from typing import Union

class Tile:

    def __init__(self, tile_id: int, data: list):
        self.tile_id = tile_id
        self.data = []
        self.width = len(data)
        for i in range(self.width):
            self.data.append([])
            for j in range(self.width):
                self.data[i].append(data[i][j])
        self.hashes = {}
        self.matches = {}
        ### LEFT
        hash_val_1 = 0
        hash_val_2 = 0
        for i in range(self.width):
            if data[i][0] == "#":
                hash_val_1 += 2 ** i
                hash_val_2 += 2 ** (self.width - 1 - i)
        self.hashes["left"] = [hash_val_1, hash_val_2]
        ### RIGHT
        hash_val_1 = 0
        hash_val_2 = 0
        for i in range(self.width):
            if data[i][9] == "#":
                hash_val_1 += 2 ** i
                hash_val_2 += 2 ** (self.width - 1 - i)
        self.hashes["right"] = [hash_val_1, hash_val_2]
        ### TOP
        hash_val_1 = 0
        hash_val_2 = 0
        for i in range(self.width):
            if data[0][i] == "#":
                hash_val_1 += 2 ** i
                hash_val_2 += 2 ** (self.width - 1 - i)
        self.hashes["top"] = [hash_val_1, hash_val_2]
        ### BOT
        hash_val_1 = 0
        hash_val_2 = 0
        for i in range(self.width):
            if data[9][i] == "#":
                hash_val_1 += 2 ** i
                hash_val_2 += 2 ** (self.width - 1 - i)
        self.hashes["bot"] = [hash_val_1, hash_val_2]

    def __eq__(self, other):
        return self.tile_id == other.tile_id

    def flip_x(self):
        new_data = []
        for row in self.data:
            new_data.append(row[::-1])
        self.data = new_data
        self.hashes["top"] = self.hashes["top"][::-1]
        self.hashes["bot"] = self.hashes["bot"][::-1]
        temp = [self.hashes["right"][0], self.hashes["right"][1]]
        self.hashes["right"] = self.hashes["left"]
        self.hashes["left"] = temp

    def flip_y(self):
        new_data = []
        for i in range(self.width - 1, -1, -1):
            new_data.append(self.data[i])
        self.data = new_data
        self.hashes["right"] = self.hashes["right"][::-1]
        self.hashes["left"] = self.hashes["left"][::-1]
        temp = [self.hashes["top"][0], self.hashes["top"][1]]
        self.hashes["top"] = self.hashes["bot"]
        self.hashes["bot"] = temp

    def rotate_right(self):
        # 0 0 becomes 9 0, 1 0 becomes 9 1
        # 0 1 becomes 8 0, 1 1 becomes 8 1
        new_data = []
        for i in range(self.width):
            new_data.append([])
            for j in range(self.width):
                new_data[i].append(self.data[self.width - 1 - j][i])
        self.data = new_data
        temp = [self.hashes["right"][1], self.hashes["right"][0]]
        self.hashes["right"] = self.hashes["top"]
        self.hashes["top"] = self.hashes["left"][::-1]
        self.hashes["left"] = self.hashes["bot"]
        self.hashes["bot"] = temp

    def rotate_left(self):
        # 0 0 becomes 0 9, 1 0 becomes 0 8
        # 0 1 becomes 1 9, 1 1 becomes 1 8
        new_data = []
        for i in range(self.width):
            new_data.append([])
            for j in range(self.width):
                new_data[i].append(self.data[j][self.width - 1 - i])
        self.data = new_data
        temp = [self.hashes["right"][0], self.hashes["right"][1]]
        self.hashes["right"] = self.hashes["bot"][::-1]
        self.hashes["bot"] = self.hashes["left"]
        self.hashes["left"] = self.hashes["top"][::-1]
        self.hashes["top"] = temp
        
    def __str__(self):
        lines = [f"Tile {self.tile_id}:"]
        for i in range(len(self.data)):
            lines.append("".join([self.data[i][j] for j in range(len(self.data[i]))]))
        to_return = "\n".join(lines)
        to_return += f"\nHashes right : {self.hashes['right']}"
        to_return += f"\nHashes left : {self.hashes['left']}"
        to_return += f"\nHashes top : {self.hashes['top']}"
        to_return += f"\nHashes bot : {self.hashes['bot']}"
        to_return += "\n"
        return to_return
        

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
    tiles = {}
    parse_tiles(raw_data.split("\n\n"), tiles)
    top_left = match_tiles_with_flip_rotate(tiles)
    two_match = []
    for tile_id in tiles:
        if len(list(tiles[tile_id].matches.keys())) == 2:
            two_match.append(tile_id)
    print(f"Corners : {', '.join([str(i) for i in two_match])}")
    result = 1
    for val in two_match:
        result *= val
    print(f"Part 1 result: {result}")

def parse_tiles(raw_tiles: list, tiles: dict) -> None:
    for raw_tile in raw_tiles:
        lines = raw_tile.split("\n")
        tile_id = int(lines[0].split(" ")[1][:-1])
        tiles[tile_id] = Tile(tile_id, lines[1:])

def match_tiles_with_flip_rotate(tiles_dict: dict) -> int:
    fully_matched = []
    tiles_count = len(list(tiles_dict))
    next_tiles = [list(tiles_dict)[0]]
    top_left_id = -1
    counter = 0
    while True:
        current = tiles_dict[next_tiles[counter]]
        for target_side in ["right", "left", "top", "bot"]:
            if target_side in current.matches:
                continue
            hash_target = current.hashes[target_side][0]
            match_id = 0
            for tile_id in tiles_dict:
                tile = tiles_dict[tile_id]
                if match_id:
                    break
                if tile_id == next_tiles[counter]:
                    continue
                if len(tile.matches) == 4:
                    continue
                for test_side in tile.hashes:
                    if match_id:
                        break
                    for val in tile.hashes[test_side]:
                        if hash_target == val:
                            match_id = tile.tile_id
                            pair(current, tile, target_side)
            if match_id:
                if match_id not in next_tiles:
                    next_tiles.append(match_id)
        fully_matched.append(current.tile_id)
        match_list = list(current.matches)
        if len(match_list) == 2:
            if "right" and "bot" in match_list:
                top_left_id = next_tiles[counter]
        if len(fully_matched) == tiles_count:
            break
        counter += 1
    return top_left_id
        
def pair(origin: Tile, match: Tile, target_side: str) -> None:
    if target_side == "right":
        test_side = "left"
    elif target_side == "top":
        test_side = "bot"
    elif target_side == "left":
        test_side = "right"
    else:
        test_side = "top"
    target_hash = origin.hashes[target_side][0]
    while target_hash not in match.hashes[test_side]:
        match.rotate_left()
    if target_hash == match.hashes[test_side][1]:
        if test_side in ["right", "left"]:
            match.flip_y()
        else:
            match.flip_x()
    origin.matches[target_side] = match.tile_id
    match.matches[test_side] = origin.tile_id
    

if __name__ == "__main__":
    print(run_script("input.txt"))