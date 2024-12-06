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

        W, H = len(inp[0]), len(inp)

        # find position of the guard
        for i in range(H):
            inp[i] = list(inp[i])
            for j in range(W):
                if inp[i][j] == "^":
                    guard = (i, j)
                    break

        visited_positions = set()
        active_direction = "up"

        while True:
            visited_positions.add(guard)
            if active_direction == "up":
                if guard[0] - 1 < 0:
                    break

                if inp[guard[0] - 1][guard[1]] == "#":
                    active_direction = "right"
                else:
                    guard = (guard[0] - 1, guard[1])

            elif active_direction == "right":
                if guard[1] + 1 >= W:
                    break

                if inp[guard[0]][guard[1] + 1] == "#":
                    active_direction = "down"
                else:
                    guard = (guard[0], guard[1] + 1)

            elif active_direction == "down":
                if guard[0] + 1 >= H:
                    break

                if inp[guard[0] + 1][guard[1]] == "#":
                    active_direction = "left"
                else:
                    guard = (guard[0] + 1, guard[1])

            else:
                if guard[1] - 1 < 0:
                    break

                if inp[guard[0]][guard[1] - 1] == "#":
                    active_direction = "up"
                else:
                    guard = (guard[0], guard[1] - 1)

        return len(visited_positions)


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
