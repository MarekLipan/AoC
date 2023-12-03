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
        result = 0
        set_of_symbols = set(["$", "+", "%", "&", "#", "-", "*", "/", "@", "="])
        adjacent_positions = set()

        for i, line in enumerate(inp):
            for j, symbol in enumerate(line):
                if symbol in set_of_symbols:
                    adjacent_positions.add((i, j - 1))
                    adjacent_positions.add((i, j + 1))

                    adjacent_positions.add((i - 1, j - 1))
                    adjacent_positions.add((i - 1, j))
                    adjacent_positions.add((i - 1, j + 1))

                    adjacent_positions.add((i + 1, j - 1))
                    adjacent_positions.add((i + 1, j))
                    adjacent_positions.add((i + 1, j + 1))

        for i, line in enumerate(inp):
            for m in re.finditer(r"\d+", line):
                for j in range(m.start(0), m.end(0)):
                    if (i, j) in adjacent_positions:
                        result += int(m.group(0))
                        break

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
