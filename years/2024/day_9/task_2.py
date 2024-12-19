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
        b1 = len(transformed_inp) - 1
        b2 = len(transformed_inp) - 1

        while True:

            # find rightmost object
            for j in range(b2, 0, -1):
                if transformed_inp[j] != ".":
                    b2 = j
                    break
            object_id = transformed_inp[b2]

            if object_id == 0:
                break

            # length of the object
            for j in range(b2, 0, -1):
                if transformed_inp[j] != object_id:
                    b1 = j + 1
                    break

            object_length = b2 - b1 + 1

            # find leftmost gap that is larger than the object
            a1 = 0
            found_large_enough_gap = False
            while a1 < b1:
                for i in range(a1, len(transformed_inp)):
                    if transformed_inp[i] == ".":
                        a1 = i
                        break
                # length of the gap
                for i in range(a1, len(transformed_inp)):
                    if transformed_inp[i] != ".":
                        a2 = i - 1
                        break
                gap_length = a2 - a1 + 1

                if gap_length >= object_length:
                    found_large_enough_gap = True
                    break
                else:
                    a1 = a2 + 1

            # swap object and gap if large enough gap is found and is still on the left of the object
            if found_large_enough_gap and a1 < b1:
                for i in range(object_length):
                    transformed_inp[a1 + i] = object_id
                    transformed_inp[b1 + i] = "."

            # move to the next object
            b2 = b1 - 1

        # checksum
        result = 0
        for i in range(len(transformed_inp)):
            if transformed_inp[i] != ".":
                result += i * transformed_inp[i]

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
