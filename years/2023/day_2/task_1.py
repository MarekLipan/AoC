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

        red_th = 12
        green_th = 13
        blue_th = 14

        result = 0

        for i in inp:
            if (
                max([int(n) for n in re.findall(" (\d+) blue", i)]) <= blue_th
                and max([int(n) for n in re.findall(" (\d+) red", i)]) <= red_th
                and max([int(n) for n in re.findall(" (\d+) green", i)]) <= green_th
            ):
                result += int(re.findall("Game (\d+)", i)[0])

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
