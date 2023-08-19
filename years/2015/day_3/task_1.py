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

        visited_houses = set()
        current_position = (0, 0)
        visited_houses.add(current_position)

        for direction in inp[0]:
            if direction == "^":
                current_position = (current_position[0], current_position[1] + 1)
            elif direction == "v":
                current_position = (current_position[0], current_position[1] - 1)
            elif direction == ">":
                current_position = (current_position[0] + 1, current_position[1])
            elif direction == "<":
                current_position = (current_position[0] - 1, current_position[1])

            visited_houses.add(current_position)

        result = len(visited_houses)

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
