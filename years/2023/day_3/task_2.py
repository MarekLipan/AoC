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
        star_pos_adj_pos_map = dict()
        star_pos_adj_part_nums = dict()

        for i, line in enumerate(inp):
            for j, symbol in enumerate(line):
                if symbol == "*":
                    star_pos_adj_pos_map[(i, j)] = set(
                        [
                            (i, j - 1),
                            (i, j + 1),
                            (i - 1, j - 1),
                            (i - 1, j),
                            (i - 1, j + 1),
                            (i + 1, j - 1),
                            (i + 1, j),
                            (i + 1, j + 1),
                        ]
                    )
                    star_pos_adj_part_nums[(i, j)] = []

        for i, line in enumerate(inp):
            for m in re.finditer(r"\d+", line):
                assign_to_stars = set()

                for j in range(m.start(0), m.end(0)):
                    for s, adj_pos in star_pos_adj_pos_map.items():
                        if (i, j) in adj_pos:
                            assign_to_stars.add(s)

                for s in assign_to_stars:
                    star_pos_adj_part_nums[s].append(m.group(0))

        result = 0
        for part_nums in star_pos_adj_part_nums.values():
            if len(part_nums) == 2:
                result += int(part_nums[0]) * int(part_nums[1])

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
