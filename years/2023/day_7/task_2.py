"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver
import itertools
import numpy as np


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        card_mapping = {
            "a": "A",
            "b": "K",
            "c": "Q",
            "d": "T",
            "e": "9",
            "f": "8",
            "g": "7",
            "h": "6",
            "i": "5",
            "j": "4",
            "k": "3",
            "l": "2",
            "m": "J",
        }

        card_mapping_reverse = {
            "A": "a",
            "K": "b",
            "Q": "c",
            "T": "d",
            "9": "e",
            "8": "f",
            "7": "g",
            "6": "h",
            "5": "i",
            "4": "j",
            "3": "k",
            "2": "l",
            "J": "m",
        }

        cards = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

        all_pairs = [(a, b) for idx, a in enumerate(cards) for b in cards[idx + 1 :]]
        all_triples = [
            (a, b, c)
            for idx, a in enumerate(cards)
            for idx2, b in enumerate(cards[idx + 1 :])
            for c in cards[idx + idx2 + 2 :]
        ]
        all_quads = [
            (a, b, c, d)
            for idx, a in enumerate(cards)
            for idx2, b in enumerate(cards[idx + 1 :])
            for idx3, c in enumerate(cards[idx + idx2 + 2 :])
            for d in cards[idx + idx2 + idx3 + 3 :]
        ]
        all_fives = [
            (a, b, c, d, e)
            for idx, a in enumerate(cards)
            for idx2, b in enumerate(cards[idx + 1 :])
            for idx3, c in enumerate(cards[idx + idx2 + 2 :])
            for idx4, d in enumerate(cards[idx + idx2 + idx3 + 3 :])
            for e in cards[idx + idx2 + idx3 + idx4 + 4 :]
        ]

        possible_hands_ranked = []

        # five of a kind
        five_of_a_kind = ["".join(5 * [c]) for c in cards]
        # J cases
        for c in cards:
            five_of_a_kind += [
                "".join(h) for h in itertools.permutations(["m"] + 4 * [c])
            ]
            five_of_a_kind += [
                "".join(h) for h in itertools.permutations(2 * ["m"] + 3 * [c])
            ]
            five_of_a_kind += [
                "".join(h) for h in itertools.permutations(3 * ["m"] + 2 * [c])
            ]
            five_of_a_kind += [
                "".join(h) for h in itertools.permutations(4 * ["m"] + [c])
            ]
        five_of_a_kind += ["mmmmm"]
        possible_hands_ranked += sorted(list(set(five_of_a_kind)))

        # four of a kind
        four_of_a_kind = []
        for p in all_pairs:
            four_of_a_kind += [
                "".join(h) for h in itertools.permutations(4 * [p[0]] + [p[1]])
            ]
            four_of_a_kind += [
                "".join(h) for h in itertools.permutations([p[0]] + 4 * [p[1]])
            ]
        # J cases
        for p in all_pairs:
            four_of_a_kind += [
                "".join(h) for h in itertools.permutations(3 * ["m"] + [p[0]] + [p[1]])
            ]
            four_of_a_kind += [
                "".join(h)
                for h in itertools.permutations(2 * ["m"] + 2 * [p[0]] + [p[1]])
            ]
            four_of_a_kind += [
                "".join(h)
                for h in itertools.permutations(2 * ["m"] + [p[0]] + 2 * [p[1]])
            ]
            four_of_a_kind += [
                "".join(h) for h in itertools.permutations(["m"] + 3 * [p[0]] + [p[1]])
            ]
            four_of_a_kind += [
                "".join(h) for h in itertools.permutations(["m"] + [p[0]] + 3 * [p[1]])
            ]
        possible_hands_ranked += sorted(list(set(four_of_a_kind)))

        # full house
        full_house = []
        for p in all_pairs:
            full_house += [
                "".join(h) for h in itertools.permutations(3 * [p[0]] + 2 * [p[1]])
            ]
            full_house += [
                "".join(h) for h in itertools.permutations(2 * [p[0]] + 3 * [p[1]])
            ]
        # J cases
        for p in all_pairs:
            full_house += [
                "".join(h)
                for h in itertools.permutations(["m"] + 2 * [p[0]] + 2 * [p[1]])
            ]
        possible_hands_ranked += sorted(list(set(full_house)))

        # three of a kind
        three_of_a_kind = []
        for t in all_triples:
            three_of_a_kind += [
                "".join(h) for h in itertools.permutations(3 * [t[0]] + [t[1]] + [t[2]])
            ]
            three_of_a_kind += [
                "".join(h) for h in itertools.permutations([t[0]] + 3 * [t[1]] + [t[2]])
            ]
            three_of_a_kind += [
                "".join(h) for h in itertools.permutations([t[0]] + [t[1]] + 3 * [t[2]])
            ]
        # J cases
        for t in all_triples:
            three_of_a_kind += [
                "".join(h)
                for h in itertools.permutations(["m"] + 2 * [t[0]] + [t[1]] + [t[2]])
            ]
            three_of_a_kind += [
                "".join(h)
                for h in itertools.permutations(["m"] + [t[0]] + 2 * [t[1]] + [t[2]])
            ]
            three_of_a_kind += [
                "".join(h)
                for h in itertools.permutations(["m"] + [t[0]] + [t[1]] + 2 * [t[2]])
            ]
            three_of_a_kind += [
                "".join(h)
                for h in itertools.permutations(2 * ["m"] + [t[0]] + [t[1]] + [t[2]])
            ]
        possible_hands_ranked += sorted(list(set(three_of_a_kind)))
        # two pairs
        two_pairs = []
        for t in all_triples:
            two_pairs += [
                "".join(h)
                for h in itertools.permutations(2 * [t[0]] + 2 * [t[1]] + [t[2]])
            ]
            two_pairs += [
                "".join(h)
                for h in itertools.permutations(2 * [t[0]] + [t[1]] + 2 * [t[2]])
            ]
            two_pairs += [
                "".join(h)
                for h in itertools.permutations([t[0]] + 2 * [t[1]] + 2 * [t[2]])
            ]
        possible_hands_ranked += sorted(list(set(two_pairs)))
        # one pair
        one_pair = []
        for q in all_quads:
            one_pair += [
                "".join(h)
                for h in itertools.permutations(2 * [q[0]] + [q[1]] + [q[2]] + [q[3]])
            ]
            one_pair += [
                "".join(h)
                for h in itertools.permutations([q[0]] + 2 * [q[1]] + [q[2]] + [q[3]])
            ]
            one_pair += [
                "".join(h)
                for h in itertools.permutations([q[0]] + [q[1]] + 2 * [q[2]] + [q[3]])
            ]
            one_pair += [
                "".join(h)
                for h in itertools.permutations([q[0]] + [q[1]] + [q[2]] + 2 * [q[3]])
            ]
        # J cases
        for q in all_quads:
            one_pair += [
                "".join(h)
                for h in itertools.permutations(
                    ["m"] + [q[0]] + [q[1]] + [q[2]] + [q[3]]
                )
            ]
        possible_hands_ranked += sorted(list(set(one_pair)))
        # high card
        high_card = []
        for f in all_fives:
            high_card += [
                "".join(h)
                for h in itertools.permutations(
                    [f[0]] + [f[1]] + [f[2]] + [f[3]] + [f[4]]
                )
            ]
        possible_hands_ranked += sorted(list(set(high_card)))

        # parse
        hands = []
        bids = []
        ranks = []

        for p in inp:
            hands.append(p.split(" ")[0])
            bids.append(int(p.split(" ")[1]))

        for h in hands:
            mapped_hand = "".join([card_mapping_reverse[c] for c in h])
            ranks.append(possible_hands_ranked.index(mapped_hand))

        ind = np.argsort(-np.array(ranks))

        return sum(np.arange(1, len(bids) + 1) * np.array(bids)[ind])


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
