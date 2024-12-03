"""
Solution for the day's puzzle
"""

import os
import re
from typing import List
from utils.solver import Solver


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        # concatenate the input
        s = "".join(inp)

        parsed_s = re.findall("mul\((\d{1,3}),(\d{1,3})\)", s)

        result = 0
        for a, b in parsed_s:
            result += int(a) * int(b)

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=False)
