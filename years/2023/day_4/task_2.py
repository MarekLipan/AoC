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

        num_sc = len(inp) * [1]

        for i, line in enumerate(inp):
            nums = re.findall("(\d+)", line.split(":")[1].split("|")[0])
            target_nums = re.findall("(\d+)", line.split(":")[1].split("|")[1])

            matches = 0
            for n in nums:
                if n in target_nums:
                    matches += 1

            # add car copies
            for m in range(1, matches + 1):
                if i + m < len(num_sc):
                    num_sc[i + m] += num_sc[i]

        return sum(num_sc)


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
