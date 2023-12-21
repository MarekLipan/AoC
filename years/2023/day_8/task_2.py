"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver
import math


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        instructions = inp[0].replace("L", "0").replace("R", "1")

        plan = {}

        for i in inp[2:]:
            plan[i[:3]] = (i[7:10], i[12:15])

        start_nodes = set()
        end_nodes = set()
        for i in plan:
            if i[2] == "A":
                start_nodes.add(i)
            if i[2] == "Z":
                end_nodes.add(i)

        print(start_nodes)

        periods = set()

        for start_node in start_nodes:
            current_node = start_node
            print(current_node)
            s = 0
            prev_s = 0
            while s < 1000000:
                current_node = plan[current_node][
                    int(instructions[s % len(instructions)])
                ]
                s += 1

                if current_node in end_nodes:
                    periods.add(s - prev_s)
                    prev_s = s

        return math.lcm(*periods)


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_test_task=True, solve_main_task=True)
