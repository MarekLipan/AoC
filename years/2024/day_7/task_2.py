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

    @staticmethod
    def recursive_add_or_multiply_or_concat(
        elements: List[int], current_total: int, possible_totals: set
    ):
        if not elements:
            possible_totals.add(current_total)
            return

        TodaySolver.recursive_add_or_multiply_or_concat(
            elements[1:], current_total + elements[0], possible_totals
        )
        TodaySolver.recursive_add_or_multiply_or_concat(
            elements[1:], current_total * elements[0], possible_totals
        )
        TodaySolver.recursive_add_or_multiply_or_concat(
            elements[1:], int(str(current_total) + str(elements[0])), possible_totals
        )

        return possible_totals

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        result = 0

        for line in inp:
            elements = list(map(int, re.findall("(\d+)", line)))

            total = elements.pop(0)

            first_element = elements.pop(0)

            possible_totals = set()

            TodaySolver.recursive_add_or_multiply_or_concat(
                elements, first_element, possible_totals
            )

            if total in possible_totals:
                result += total

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
