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

        inp = [int(i) for i in inp[0]]
        L = len(inp)

        # transform input
        transformed_inp = inp[0] * [0]

        object_id = 1
        for i in range(1, L, 2):
            transformed_inp.extend(inp[i] * ["."])
            transformed_inp.extend(inp[i + 1] * [object_id])
            object_id += 1

        # fragmentation
        a = 0
        b = len(transformed_inp) - 1

        while a <= b:

            # find first gap
            for i in range(a, len(transformed_inp)):
                if transformed_inp[i] == ".":
                    a = i
                    break
            # find last object
            for j in range(b, 0, -1):
                if transformed_inp[j] != ".":
                    b = j
                    break
            # swap
            if a < b:
                transformed_inp[a], transformed_inp[b] = (
                    transformed_inp[b],
                    transformed_inp[a],
                )
                a += 1
                b -= 1

        # checksum
        result = 0
        for i in range(len(transformed_inp)):
            if transformed_inp[i] != ".":
                result += i * transformed_inp[i]

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
