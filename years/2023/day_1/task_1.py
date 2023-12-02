"""
Solution for the day's puzzle
"""

import sys

sys.path.append("/Users/marek.lipan/Desktop/Projects/AoC")


import os
from typing import List
from utils.solver import Solver


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        result = 0

        for line in inp:
            # first number
            for i in line:
                if i.isdigit():
                    first_num = i
                    break
            # second number
            for i in line[::-1]:
                if i.isdigit():
                    second_num = i
                    break
            result += int(first_num + second_num)

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
