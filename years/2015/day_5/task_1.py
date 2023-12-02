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

        result = 0

        for s in inp:
            vowel_condition = False
            twice_in_row_letter_condition = False
            forbidden_string_condition = False
            vowels = 0

            for l in s:
                if l in ["a", "e", "i", "o", "u"]:
                    vowels += 1

            if vowels >= 3:
                vowel_condition = True

            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    twice_in_row_letter_condition = True
                if s[i : i + 2] in ["ab", "cd", "pq", "xy"]:
                    forbidden_string_condition = True

            if (
                vowel_condition
                and twice_in_row_letter_condition
                and not forbidden_string_condition
            ):
                result += 1

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
