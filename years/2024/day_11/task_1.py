"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver


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

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        stones = [int(i) for i in inp[0].split(" ")]

        for _ in range(25):
            stones = self.blink(stones)

        return len(stones)


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
