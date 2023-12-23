"""
Solution for the day's puzzle
"""

import os
from typing import List
import numpy as np
from utils.solver import Solver


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        pipe_map = []
        for line in inp:
            pipe_map.append(list(line))

        pipe_map = np.vstack(pipe_map)

        def single_move(prev_coords: tuple, current_coords: tuple) -> tuple:
            """Based on previous and current coordinates, return next coordinates"""

            current_symbol = pipe_map[current_coords[0], current_coords[1]]

            diff = (
                current_coords[0] - prev_coords[0],
                current_coords[1] - prev_coords[1],
            )
            if diff == (0, 1):
                inc_direction = "right"
            elif diff == (0, -1):
                inc_direction = "left"
            elif diff == (1, 0):
                inc_direction = "down"
            elif diff == (-1, 0):
                inc_direction = "up"

            if current_symbol == "|":
                if inc_direction == "down":
                    next_coords = (current_coords[0] + 1, current_coords[1])
                elif inc_direction == "up":
                    next_coords = (current_coords[0] - 1, current_coords[1])
            elif current_symbol == "-":
                if inc_direction == "right":
                    next_coords = (current_coords[0], current_coords[1] + 1)
                elif inc_direction == "left":
                    next_coords = (current_coords[0], current_coords[1] - 1)
            elif current_symbol == "L":
                if inc_direction == "down":
                    next_coords = (current_coords[0], current_coords[1] + 1)
                elif inc_direction == "left":
                    next_coords = (current_coords[0] - 1, current_coords[1])
            elif current_symbol == "J":
                if inc_direction == "down":
                    next_coords = (current_coords[0], current_coords[1] - 1)
                elif inc_direction == "right":
                    next_coords = (current_coords[0] - 1, current_coords[1])
            elif current_symbol == "7":
                if inc_direction == "right":
                    next_coords = (current_coords[0] + 1, current_coords[1])
                elif inc_direction == "up":
                    next_coords = (current_coords[0], current_coords[1] - 1)
            elif current_symbol == "F":
                if inc_direction == "up":
                    next_coords = (current_coords[0], current_coords[1] + 1)
                elif inc_direction == "left":
                    next_coords = (current_coords[0] + 1, current_coords[1])

            return current_coords, next_coords

        # single_move((0, 0), (0, 1))
        # find S
        start_coords = np.where(pipe_map == "S")
        start_coords = (start_coords[0][0], start_coords[1][0])

        prev_coords, next_coords = start_coords, (
            start_coords[0] + 1,  # custom modified based on my personal input
            start_coords[1],
        )

        s = 1
        while next_coords != start_coords:
            prev_coords, next_coords = single_move(prev_coords, next_coords)
            s += 1

        return int(s / 2)


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
