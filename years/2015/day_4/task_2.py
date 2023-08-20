"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver

import hashlib


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        result = 0
        hashed_input = hashlib.md5((inp[0] + str(result)).encode()).hexdigest()

        while hashed_input[:6] != "000000":
            result += 1
            hashed_input = hashlib.md5((inp[0] + str(result)).encode()).hexdigest()

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
