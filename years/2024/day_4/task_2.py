"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        W = len(inp[0])
        H = len(inp)

        result = 0
        ms_set = set(["M", "S"])

        for i in range(H):
            for j in range(W):
                if (
                    inp[i][j] == "A"
                    and (i + 1 < H)
                    and (j + 1 < W)
                    and (i - 1 >= 0)
                    and (j - 1 >= 0)
                ):
                    set_diagonal_left_upwards = set(
                        [inp[i - 1][j - 1], inp[i + 1][j + 1]]
                    )
                    set_diagonal_right_downwards = set(
                        [inp[i + 1][j - 1], inp[i - 1][j + 1]]
                    )

                    if (
                        set_diagonal_left_upwards == ms_set
                        and set_diagonal_right_downwards == ms_set
                    ):
                        result += 1
        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
