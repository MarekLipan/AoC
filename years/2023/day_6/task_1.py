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

        times = [int(i) for i in re.findall("(\d+)", inp[0])]
        record_distances = [int(i) for i in re.findall("(\d+)", inp[1])]

        result = 1

        for r in range(len(times)):
            distances = []
            for hold_time in range(times[r]):
                remaining_time = times[r] - hold_time
                distances.append(hold_time * remaining_time)

            w = 0
            for d in distances:
                if d > record_distances[r]:
                    w += 1

            result *= w

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
