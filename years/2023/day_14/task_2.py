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

        num_rows = array.shape[0]
        num_cols = array.shape[1]

        stable_stone_indices = np.where(array == "#")
        dynamic_stone_indices = np.where(array == "O")

        # north
        for c in range(num_cols):
            sel_stable_stone_indices = stable_stone_indices[0][
                np.where(stable_stone_indices[1] == c)
            ]
            sel_dynamic_stone_indices = dynamic_stone_indices[0][
                np.where(dynamic_stone_indices[1] == c)
            ]
            moved_dynamic_stone_indices = []
            for i in sel_dynamic_stone_indices:
                lower_bound = -1
                for upper_bound in list(sel_stable_stone_indices) + [num_rows]:
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
            # move dynamic stone indices
            dynamic_stone_indices[0][
                np.where(dynamic_stone_indices[1] == c)
            ] = moved_dynamic_stone_indices

        print(dynamic_stone_indices)

        # west
        for r in range(num_rows):
            sel_stable_stone_indices = stable_stone_indices[1][
                np.where(stable_stone_indices[0] == r)
            ]
            sel_dynamic_stone_indices = dynamic_stone_indices[1][
                np.where(dynamic_stone_indices[0] == r)
            ]
            moved_dynamic_stone_indices = []
            for i in sel_dynamic_stone_indices:
                lower_bound = -1
                for upper_bound in list(sel_stable_stone_indices) + [num_cols]:
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
            # move dynamic stone indices
            dynamic_stone_indices[1][
                np.where(dynamic_stone_indices[0] == r)
            ] = moved_dynamic_stone_indices

        print(dynamic_stone_indices)

        # south
        for c in range(num_cols):
            sel_stable_stone_indices = stable_stone_indices[0][
                np.where(stable_stone_indices[1] == c)
            ]
            sel_dynamic_stone_indices = dynamic_stone_indices[0][
                np.where(dynamic_stone_indices[1] == c)
            ]
            moved_dynamic_stone_indices = []
            for i in sel_dynamic_stone_indices:
                lower_bound = num_rows
                for upper_bound in list(sel_stable_stone_indices)[::-1] + [-1]:
                    if lower_bound > i > upper_bound:
                        if len(moved_dynamic_stone_indices) == 0:
                            moved_dynamic_stone_indices.append(lower_bound - 1)
                        else:
                            moved_dynamic_stone_indices.append(
                                min(
                                    lower_bound - 1, moved_dynamic_stone_indices[-1] - 1
                                )
                            )
                        break
                    else:
                        lower_bound = upper_bound

            # move dynamic stone indices
            dynamic_stone_indices[0][
                np.where(dynamic_stone_indices[1] == c)
            ] = moved_dynamic_stone_indices

        print(dynamic_stone_indices)

        return sum(num_rows - dynamic_stone_indices[0])


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=False)
