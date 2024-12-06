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

    @staticmethod
    def is_correct(u: List[int], rules: List[List[int]]):
        """Check if the update follows all rules and is correct"""
        correct = True
        for r in rules:
            a, b = r

            if a not in u or b not in u:
                continue

            a_index = u.index(a)
            b_index = u.index(b)
            if a_index > b_index:
                correct = False
                break
        return correct

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        rules = []
        updates = []

        i = inp.pop(0)
        while i != "":
            a, b = i.split("|")
            a = int(a)
            b = int(b)
            rules.append([a, b])
            i = inp.pop(0)

        for i in inp:
            updates.append(list(map(int, i.split(","))))

        incorrect_updates = []
        for u in updates:
            if not self.is_correct(u, rules):
                incorrect_updates.append(u)

        correctly_sorted_updates = []
        for u in incorrect_updates:
            correctly_sorted = False
            while correctly_sorted is False:
                correctly_sorted = True
                for r in rules:
                    a, b = r
                    if a not in u or b not in u:
                        continue

                    a_index = u.index(a)
                    b_index = u.index(b)
                    if a_index > b_index:
                        correctly_sorted = False
                        # swap a and b
                        u[a_index], u[b_index] = u[b_index], u[a_index]
                        break
            correctly_sorted_updates.append(u)

        result = 0
        for u in correctly_sorted_updates:
            result += u[len(u) // 2]

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
