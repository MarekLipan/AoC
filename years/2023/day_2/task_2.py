"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver
import re


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        result = 0

        for i in inp:
            result += (
                max([int(n) for n in re.findall(" (\d+) blue", i)])
                * max([int(n) for n in re.findall(" (\d+) red", i)])
                * max([int(n) for n in re.findall(" (\d+) green", i)])
            )

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
