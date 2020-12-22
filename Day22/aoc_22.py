import time
from typing import Union
from collections import deque

class CardDeck:

    def __init__(self):
        self.cards = deque([])

    def put(self, card: int) -> None:
        self.cards.append(card)
    
    def get(self) -> int:
        return self.cards.popleft()

    def empty(self) -> bool:
        return len(self.cards) == 0

    def size(self) -> int:
        return len(self.cards)

    def score(self) -> int:
        card_count = len(self.cards)
        return sum([self.cards[i] * (card_count - i) for i in range(card_count)])

    def sub_deck(self, size: int):
        new_deck = CardDeck()
        for i in range(size):
            new_deck.put(self.cards[i])
        return new_deck

    def copy(self):
        return self.sub_deck(len(self.cards))

    def __eq__(self, other) -> bool:
        if len(self.cards) != len(other.cards):
            return False
        for i in range(len(self.cards)):
            if self.cards[i] != other.cards[i]:
                return False
        return True

    def __str__(self) -> str:
        return ", ".join([str(i) for i in self.cards])

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
    winner = resolve_game(p1_deck, p2_deck)
    return p1_deck.score() if winner == 1 else p2_deck.score()

def resolve_game(p1_deck: CardDeck, p2_deck: CardDeck) -> int:
    states = set()
    while not p1_deck.empty() and not p2_deck.empty():
        current_state = (p1_deck.score(), p2_deck.score())
        if current_state in states:
            return 1
        states.add(current_state)
        resolve_turn(p1_deck, p2_deck)
    return 1 if p2_deck.empty() else 2

def resolve_turn(p1_deck: CardDeck, p2_deck: CardDeck) -> None:
    p1_card = p1_deck.get()
    p2_card = p2_deck.get()
    if p1_card <= p1_deck.size() and p2_card <= p2_deck.size():
        sub_winner = resolve_game(p1_deck.sub_deck(p1_card), p2_deck.sub_deck(p2_card))
        if sub_winner == 1:
            p1_deck.put(p1_card)
            p1_deck.put(p2_card)
        else:
            p2_deck.put(p2_card)
            p2_deck.put(p1_card)
    else:
        if p1_card > p2_card:
            p1_deck.put(p1_card)
            p1_deck.put(p2_card)
        else:
            p2_deck.put(p2_card)
            p2_deck.put(p1_card)

def parse_deck(raw_deck: list) -> CardDeck:
    deck = CardDeck()
    for raw_card in raw_deck.split("\n")[1:]:
        deck.put(int(raw_card))
    return deck

if __name__ == "__main__":
    print(run_script("input.txt"))