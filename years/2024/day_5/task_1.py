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

        print(rules)
        print("----")
        print(updates)

        result = 0
        for u in updates:
            print(f"Checking {u}")

            correct = True
            for r in rules:
                a, b = r

                if a not in u or b not in u:
                    continue

                a_index = u.index(a)
                b_index = u.index(b)
                if a_index > b_index:
                    print(f"Breach. Rule {r} not satisfied")
                    correct = False
                    break

            # add middle element to result
            if correct:
                print(f"Correct, adding {u[len(u) // 2]}")
                result += u[len(u) // 2]

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
