"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver
import numpy as np


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        result = 0

        for line in inp:
            parsed_line = np.array([int(i) for i in line.split(" ")])

            # diff step
            diff_lines = [parsed_line]
            diff_line = np.diff(parsed_line)
            while not np.all(diff_line == 0):
                diff_lines.append(diff_line)
                diff_line = np.diff(diff_line)

            # pred step
            next_step = 0
            for diff_line in diff_lines[::-1]:
                next_step = diff_line[0] - next_step

            result += next_step

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
