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

        for i in range(H):
            for j in range(W):
                # horizontal rightwards
                if j + 3 < W:
                    if (
                        inp[i][j] == "X"
                        and inp[i][j + 1] == "M"
                        and inp[i][j + 2] == "A"
                        and inp[i][j + 3] == "S"
                    ):
                        result += 1
                # horizontal leftwards
                if j - 3 >= 0:
                    if (
                        inp[i][j] == "X"
                        and inp[i][j - 1] == "M"
                        and inp[i][j - 2] == "A"
                        and inp[i][j - 3] == "S"
                    ):
                        result += 1
                # vertical downwards
                if i + 3 < H:
                    if (
                        inp[i][j] == "X"
                        and inp[i + 1][j] == "M"
                        and inp[i + 2][j] == "A"
                        and inp[i + 3][j] == "S"
                    ):
                        result += 1
                # vertical upwards
                if i - 3 >= 0:
                    if (
                        inp[i][j] == "X"
                        and inp[i - 1][j] == "M"
                        and inp[i - 2][j] == "A"
                        and inp[i - 3][j] == "S"
                    ):
                        result += 1
                # diagonal rightwards downwards
                if i + 3 < H and j + 3 < W:
                    if (
                        inp[i][j] == "X"
                        and inp[i + 1][j + 1] == "M"
                        and inp[i + 2][j + 2] == "A"
                        and inp[i + 3][j + 3] == "S"
                    ):
                        result += 1
                # diagonal rightwards upwards
                if i - 3 >= 0 and j + 3 < W:
                    if (
                        inp[i][j] == "X"
                        and inp[i - 1][j + 1] == "M"
                        and inp[i - 2][j + 2] == "A"
                        and inp[i - 3][j + 3] == "S"
                    ):
                        result += 1
                # diagonal leftwards downwards
                if i + 3 < H and j - 3 >= 0:
                    if (
                        inp[i][j] == "X"
                        and inp[i + 1][j - 1] == "M"
                        and inp[i + 2][j - 2] == "A"
                        and inp[i + 3][j - 3] == "S"
                    ):
                        result += 1
                # diagonal leftwards upwards
                if i - 3 >= 0 and j - 3 >= 0:
                    if (
                        inp[i][j] == "X"
                        and inp[i - 1][j - 1] == "M"
                        and inp[i - 2][j - 2] == "A"
                        and inp[i - 3][j - 3] == "S"
                    ):
                        result += 1

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
