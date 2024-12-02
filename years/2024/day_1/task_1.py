"""
Solution for the day's puzzle
"""

import re
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

        list_a = []
        list_b = []

        for line in inp:
            a, b = re.findall("(\d+)", line)

            list_a.append(int(a))
            list_b.append(int(b))

        list_a.sort()
        list_b.sort()

        array_a = np.array(list_a)
        array_b = np.array(list_b)

        abs_diff = np.abs(array_a - array_b)

        sum_abs_diff = np.sum(abs_diff)

        return sum_abs_diff


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
