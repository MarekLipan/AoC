"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver
import re
from tqdm import tqdm


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    @staticmethod
    def run(A):
        out = (A % 8 ^ 1 ^ (A // 2 ** (A % 8 ^ 1)) ^ 4) % 8
        return A // 8, out

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""
        program = list(map(int, re.findall("(\d+)", inp[4])))

        print(program)

        reverse_program = program[::-1]

        print(len(reverse_program))

        o_a = 0
        for o in reverse_program:
            print(f"Target A: {o_a} Target Output: {o}")
            input_a = o_a * 8 - 1
            out = -1
            output_a = -1
            while out != o:
                input_a += 1
                output_a, out = TodaySolver.run(input_a)

                print(f"A in: {input_a}, Output: {output_a}, A out: {out}")

            o_a = input_a

        return input_a


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True, solve_test_task=False)
