"""
Solution for the day's puzzle
"""

import os
from typing import List


class Solver:
    """
    Contains input and solution for the day's puzzle
    """

    def __init__(self, path: str):
        with open(
            os.path.join(path, "../test_input.txt"),
            "r",
            encoding="utf-8",
        ) as input_file:
            self.task_test_input = input_file.read().splitlines()

        with open(
            os.path.join(path, "../input.txt"),
            "r",
            encoding="utf-8",
        ) as input_file:
            self.task_input = input_file.read().splitlines()

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        print(inp)

        return None

    def solve_and_print_result(self, solve_main_task: bool):
        """
        Function to solve the puzzle and print the solution
        """

        print(f"Test input Solution: {self.solution(self.task_test_input)}")
        if solve_main_task:
            print(f"Solution: {self.solution(self.task_input)}")
