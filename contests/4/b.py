import random
import sys
from typing import Any, Dict
INITIAL_CARDS_COUNT = {2: 8, 3: 7, 4: 6}
BUILDING_COST_RANGES = [(10, 25), (25, 50), (50, 100), (100, 200)]
PLAYER_COLORS = ['red', 'green', 'blue', 'yellow']


def generate(num_players: int) -> Dict[str, Any]:
    building_costs = [random.randint(low, high) for low, high in BUILDING_COST_RANGES[:num_players]]

    initial_cards_count = INITIAL_CARDS_COUNT[num_players]
    card_deck = list(range(1, 43))
    random.shuffle(card_deck)
    players_cards = [card_deck.pop(0) for _ in range(initial_cards_count * num_players)]

    random.shuffle(PLAYER_COLORS)
    players = [{'color': color, 'cards': players_cards[i::num_players]} for i, color in enumerate(PLAYER_COLORS[:num_players])]

    return {'players': players, 'costs': building_costs, 'card_deck': card_deck}


def main():
    exec(sys.stdin.read())


if __name__ == '__main__':
    main()
