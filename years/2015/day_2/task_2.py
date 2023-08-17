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

            list_of_sides = [l, w, h]
            list_of_sides.sort()

            result += sum(list_of_sides[:2]) * 2 + l * w * h

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
