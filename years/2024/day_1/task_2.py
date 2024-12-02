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

        similarity_score = 0

        for a in list_a:
            for b in list_b:
                if a == b:
                    similarity_score += a

        return similarity_score


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
