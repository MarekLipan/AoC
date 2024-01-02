"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver
import re
from itertools import combinations
from tqdm import tqdm
import time


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        def create_pattern(blocks_left, num_free_dots_left, current_pattern):
            nonlocal memo

            if (blocks_left, num_free_dots_left) in memo:
                return memo[(blocks_left, num_free_dots_left)]
            else:
                memo[(blocks_left, num_free_dots_left)] = 0

            if blocks_left == 0:
                # possible_patterns.append(current_pattern + (num_free_dots_left * "."))
                if invalid_pattern(
                    current_pattern + (num_free_dots_left * "."), template, blocks
                ):
                    return 0
                memo[(blocks_left, num_free_dots_left)] += 1
                return 1
            for d in range(num_free_dots_left + 1):
                new_addition = (
                    (d * ".")
                    + (blocks[-blocks_left] * "#")
                    + ("." if blocks_left > 1 else "")
                )

                if invalid_pattern(
                    current_pattern + new_addition,
                    template[: len(current_pattern + new_addition)],
                    blocks[: (len(blocks) - blocks_left + 1)],
                ):
                    continue

                memo[(blocks_left, num_free_dots_left)] += create_pattern(
                    blocks_left - 1,
                    num_free_dots_left - d,
                    current_pattern + new_addition,
                )

            return memo[(blocks_left, num_free_dots_left)]

        def invalid_pattern(pattern, template, blocks):
            for i in range(len(pattern)):
                if template[i] != "?" and template[i] != pattern[i]:
                    return True
            # check if number and length of blocks is correct
            blocks_in_pattern = re.findall("#+", pattern)
            if len(blocks_in_pattern) != len(blocks):
                return True
            for i in range(len(blocks)):
                if len(blocks_in_pattern[i]) != blocks[i]:
                    return True
            return False

        result = 0
        for line in tqdm(inp):
            single_blocks = [int(n) for n in re.findall("(\d+)", line)]
            single_template = line.split(" ")[0]

            # "unfold" the template and the blocks
            blocks = single_blocks * 5
            template = "?".join([single_template] * 5)

            len_template = len(template)
            num_blocks = len(blocks)
            num_free_dots = len_template - sum(blocks) - (len(blocks) - 1)

            # create all possible combinations of blocks and free dots
            memo = {}
            create_pattern(num_blocks, num_free_dots, "")
            result += memo[(num_blocks, num_free_dots)]

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
