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

        # parse input into columns
        rows = [list(line.strip()) for line in inp]
        array = np.vstack(rows)

        result = 0

        num_rows = array.shape[0]

        for c in range(array.shape[1]):
            stable_stone_indices = np.where(array[:, c] == "#")[0]
            dynamic_stone_indices = np.where(array[:, c] == "O")[0]
            moved_dynamic_stone_indices = []
            for i in dynamic_stone_indices:
                lower_bound = -1
                for upper_bound in list(stable_stone_indices) + [num_rows]:
                    if lower_bound < i < upper_bound:
                        if len(moved_dynamic_stone_indices) == 0:
                            moved_dynamic_stone_indices.append(lower_bound + 1)
                        else:
                            moved_dynamic_stone_indices.append(
                                max(
                                    lower_bound + 1, moved_dynamic_stone_indices[-1] + 1
                                )
                            )
                        break
                    else:
                        lower_bound = upper_bound

            for s in moved_dynamic_stone_indices:
                result += num_rows - s

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
