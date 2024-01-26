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

        # parse input to numpy arrays
        arrays = []
        current_array = []
        for line in inp:
            if line == "":
                arrays.append(np.vstack(current_array))
                current_array = []
            else:
                current_array.append(list(line))
        arrays.append(np.vstack(current_array))

        result = 0
        for a in arrays:
            rows, cols = a.shape

            # check for vertical symmetry
            for c in range(1, cols):
                cols_to_check = min(c, cols - c)
                if np.array_equal(
                    a[:, (c - cols_to_check) : c],
                    a[:, c : (c + cols_to_check)][:, ::-1],
                ):
                    result += c
                    break

            # check for horizontal symmetry
            for r in range(1, rows):
                rows_to_check = min(r, rows - r)
                if np.array_equal(
                    a[(r - rows_to_check) : r, :],
                    a[r : (r + rows_to_check), :][::-1, :],
                ):
                    result += 100 * r
                    break

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
