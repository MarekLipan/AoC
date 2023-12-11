"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver

import re
import math


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        time = int("".join(re.findall("(\d+)", inp[0])))
        record_distance = int("".join(re.findall("(\d+)", inp[1])))

        sol1 = (time - math.sqrt((time**2) - 4 * record_distance)) / 2
        sol2 = (time + math.sqrt((time**2) - 4 * record_distance)) / 2

        return int(sol2) - int(sol1)


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
