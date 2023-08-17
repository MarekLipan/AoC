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

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        result = 0

        for s in inp:
            l, w, h = s.split("x")
            l, w, h = int(l), int(w), int(h)

            area = 2 * l * w + 2 * w * h + 2 * h * l
            slack = min(l * w, w * h, h * l)

            result += area + slack

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
