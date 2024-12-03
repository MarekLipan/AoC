"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver
import numpy as np
import re


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    @staticmethod
    def is_safe(report: np.ndarray) -> bool:
        """Check if the report is safe"""
        differences = np.diff(report)

        if all(
            (difference >= 1) and (difference <= 3) for difference in differences
        ) or all(
            (difference <= -1) and (difference >= -3) for difference in differences
        ):
            return True

        return False

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        total_safe = 0

        for line in inp:
            report = list(map(int, re.findall("(\d+)", line)))

            # print(f"Original Report: {report}")

            # leave out always one element
            for i in range(len(report)):
                safe = self.is_safe(np.array(report[:i] + report[i + 1 :]))
                if safe:
                    # print(f"Safe Report: {report[:i] + report[i + 1 :]}")
                    total_safe += 1
                    break

        return total_safe


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
