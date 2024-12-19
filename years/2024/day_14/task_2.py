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

    @staticmethod
    def one_step(
        positions: List[tuple], velocities: List[tuple], H: int, W: int
    ) -> List[tuple]:
        new_positions = []
        for i, p in enumerate(positions):
            y, x = p
            vy, vx = velocities[i]

            x = x + vx
            if x < 0:
                x = W + x
            elif x >= W:
                x = x - W

            y = y + vy
            if y < 0:
                y = H + y
            elif y >= H:
                y = y - H

            new_positions.append((y, x))

        return new_positions

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        H = 103
        W = 101
        middle_x = W // 2
        middle_y = H // 2

        positions = []
        velocities = []

        s = 0

        for i in inp:
            x, y, vx, vy = map(int, re.findall(r"-?\d+", i))

            positions.append((y, x))
            velocities.append((vy, vx))

        while True:
            s += 1

            if s >= 10403:
                return "Past the limit"

            positions = self.one_step(positions, velocities, H, W)

            unique_positions = list(set(positions))

            # stop if there is a point which has at least 15 point directly next to it
            for p in unique_positions:
                y, x = p
                if (
                    (y, x + 1) in unique_positions
                    and (y, x + 2) in unique_positions
                    and (y, x + 3) in unique_positions
                    and (y, x + 4) in unique_positions
                    and (y, x + 5) in unique_positions
                    and (y, x + 6) in unique_positions
                    and (y, x + 7) in unique_positions
                    and (y, x + 8) in unique_positions
                    and (y, x + 9) in unique_positions
                    and (y, x + 10) in unique_positions
                    and (y, x + 11) in unique_positions
                    and (y, x + 12) in unique_positions
                    and (y, x + 13) in unique_positions
                    and (y, x + 14) in unique_positions
                    and (y, x + 15) in unique_positions
                ):

                    # store the field with the final positions as a text file
                    with open(
                        "/Users/marek.lipan/Desktop/Projects/AoC/years/2024/day_14/task_2_debug.txt",
                        "w",
                        encoding="utf-8",
                    ) as f:
                        for i in range(H):
                            for j in range(W):
                                if (i, j) in positions:
                                    f.write("#")
                                else:
                                    f.write(".")
                            f.write("\n")

                    return s


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
