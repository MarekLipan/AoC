"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver
import re
from itertools import combinations


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        def select_free_dots(blocks_left, num_free_dots_left, current_pattern):
            if blocks_left == 0:
                possible_free_dot_patterns.append(
                    current_pattern + [num_free_dots_left]
                )
                return
            for d in range(num_free_dots_left + 1):
                select_free_dots(
                    blocks_left - 1, num_free_dots_left - d, current_pattern + [d]
                )

        result = 0
        for line in inp:
            blocks = [int(n) for n in re.findall("(\d+)", line)]
            template = line.split(" ")[0]
            len_template = len(template)
            num_blocks = len(blocks)
            num_free_dots = len_template - sum(blocks) - (len(blocks) - 1)

            # gerate all possible patters for free dots
            possible_free_dot_patterns = []

            select_free_dots(num_blocks, num_free_dots, [])

            # create all possible combinations of blocks and free dots
            possible_patterns = []
            for free_dot_pattern in possible_free_dot_patterns:
                pattern = ""
                for i in range(num_blocks + 1):
                    pattern += "." * free_dot_pattern[i]
                    if i < num_blocks:
                        pattern += "#" * blocks[i]
                        if i < num_blocks - 1:
                            pattern += "."
                possible_patterns.append(pattern)

            # keep only valid patterns based on the template
            valid_patterns = []
            for pattern in possible_patterns:
                valid = True
                for i in range(len_template):
                    if template[i] != "?" and template[i] != pattern[i]:
                        valid = False
                        break
                if valid:
                    valid_patterns.append(pattern)

            result += len(valid_patterns)

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
