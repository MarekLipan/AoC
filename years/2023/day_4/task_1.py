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

        for line in inp:
            nums = re.findall("(\d+)", line.split(":")[1].split("|")[0])
            target_nums = re.findall("(\d+)", line.split(":")[1].split("|")[1])

            matches = 0
            for n in nums:
                if n in target_nums:
                    matches += 1

            if matches > 0:
                result += 2 ** (matches - 1)

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
