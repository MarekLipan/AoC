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

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        machines = {}
        machine_id = 0
        for i in range(0, len(inp), 4):
            a_x, a_y = list(map(int, re.findall("(\d+)", inp[i])))
            b_x, b_y = list(map(int, re.findall("(\d+)", inp[i + 1])))
            prize_x, prize_y = list(map(int, re.findall("(\d+)", inp[i + 2])))
            machines[machine_id] = {
                "a_x": a_x,
                "a_y": a_y,
                "b_x": b_x,
                "b_y": b_y,
                "prize_x": prize_x,
                "prize_y": prize_y,
            }
            machine_id += 1

        result = 0
        result_2 = 0

        tolerance = 1e-9  # Define a small tolerance value

        for m_id, m in machines.items():

            cheapest_combination = None
            cheapest_cost = None

            for a in range(101):
                for b in range(101):
                    x = a * m["a_x"] + b * m["b_x"]
                    y = a * m["a_y"] + b * m["b_y"]

                    if x == m["prize_x"] and y == m["prize_y"]:
                        cost = 3 * a + b
                        if cheapest_cost is None or cost < cheapest_cost:
                            cheapest_cost = cost
                            cheapest_combination = (a, b)

            if cheapest_combination is not None:
                result += cheapest_cost

            a = (m["prize_y"] - (m["prize_x"] * m["b_y"] / m["b_x"])) / (
                m["a_y"] - (m["a_x"] * m["b_y"] / m["b_x"])
            )

            b = (m["prize_x"] - a * m["a_x"]) / m["b_x"]

            # Check if a and b are close enough to integers
            is_a_integer = abs(a - round(a)) < tolerance
            is_b_integer = abs(b - round(b)) < tolerance

            if is_a_integer and is_b_integer:
                a = round(a)
                b = round(b)
                result_2 += 3 * a + b

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
