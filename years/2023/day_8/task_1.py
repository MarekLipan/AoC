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

        print(inp)

        return None


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=False)
