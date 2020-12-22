import time
from typing import Union
from queue import Queue

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
    raw_deck_p1, raw_deck_p2 = raw_data.split("\n\n")
    p1_deck = parse_deck(raw_deck_p1)
    p2_deck = parse_deck(raw_deck_p2)
    while not p1_deck.empty() and not p2_deck.empty():
        p1_card = p1_deck.get()
        p2_card = p2_deck.get()
        if p1_card > p2_card:
            p1_deck.put(p1_card)
            p1_deck.put(p2_card)
        else:
            p2_deck.put(p2_card)
            p2_deck.put(p1_card)
    score = 0
    if p1_deck.empty():
        winning_deck = p2_deck
    else:
        winning_deck = p1_deck
    score_factor = winning_deck.qsize()
    while not winning_deck.empty():
        score += score_factor * winning_deck.get()
        score_factor -= 1
    return score


def parse_deck(raw_deck: list) -> Queue:
    deck = Queue()
    for raw_card in raw_deck.split("\n")[1:]:
        deck.put(int(raw_card))
    return deck

if __name__ == "__main__":
    print(run_script("input.txt"))