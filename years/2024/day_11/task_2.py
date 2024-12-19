"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver
from tqdm import tqdm


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    @staticmethod
    def blink(stones: List[int]):
        """Blinking function"""

        new_stones = []
        for s in stones:
            # first rule
            if s == 0:
                new_stones.append(1)
                continue
            # second rule
            s_string = str(s)
            num_digits = len(s_string)
            half_num_digits = int(num_digits / 2)
            if num_digits % 2 == 0:
                a_s = int(s_string[:half_num_digits])
                b_s = int(s_string[half_num_digits:])
                new_stones.append(a_s)
                new_stones.append(b_s)
                continue
            # third rule
            new_stones.append(s * 2024)

        return new_stones

    def blink_25_times(self, stones: List[int]):
        """Blinking function"""

        for _ in range(25):
            stones = self.blink(stones)

        return stones

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""
        original_stones = [int(i) for i in inp[0].split(" ")]

        stone_dict_25_blinks = {}
        # list of stones after 25 blinks
        after_25_blinks = self.blink_25_times(original_stones)
        unique_after_25_blinks = list(set(after_25_blinks))

        for stone in tqdm(unique_after_25_blinks):
            stone_dict_25_blinks[stone] = self.blink_25_times([stone])

        # list of stones after 50 blinks
        after_50_blinks = []
        for stone in tqdm(after_25_blinks):
            after_50_blinks.extend(stone_dict_25_blinks[stone])

        result = 0
        for stone in tqdm(after_50_blinks):
            if stone in stone_dict_25_blinks:
                result += len(stone_dict_25_blinks[stone])
            else:
                stone_dict_25_blinks[stone] = self.blink_25_times([stone])
                result += len(stone_dict_25_blinks[stone])

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=False)
