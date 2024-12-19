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

        H = 103
        W = 101

        final_positions = []

        for i in inp:
            x, y, vx, vy = map(int, re.findall(r"-?\d+", i))

            current_position = (y, x)

            for _ in range(100):
                y, x = current_position

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

                current_position = (y, x)

            final_positions.append(current_position)

        first_quadrant = 0
        second_quadrant = 0
        third_quadrant = 0
        fourth_quadrant = 0

        middle_x = W // 2
        middle_y = H // 2

        for p in final_positions:
            if p[0] == middle_y or p[1] == middle_x:
                continue

            if p[0] < middle_y:
                if p[1] < middle_x:
                    first_quadrant += 1
                else:
                    second_quadrant += 1
            else:
                if p[1] < middle_x:
                    third_quadrant += 1
                else:
                    fourth_quadrant += 1

        result = first_quadrant * fourth_quadrant * second_quadrant * third_quadrant

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
