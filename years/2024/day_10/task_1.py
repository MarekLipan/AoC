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
    def search_route(inp, current_value, i, j, W, H, reachable_positions):
        if current_value == 9:
            reachable_positions.add((i, j))
            return reachable_positions

        next_value = current_value + 1

        possible_next_positions = []
        if i > 0 and inp[i - 1][j] == next_value:
            possible_next_positions.append((i - 1, j))
        if i < H - 1 and inp[i + 1][j] == next_value:
            possible_next_positions.append((i + 1, j))
        if j > 0 and inp[i][j - 1] == next_value:
            possible_next_positions.append((i, j - 1))
        if j < W - 1 and inp[i][j + 1] == next_value:
            possible_next_positions.append((i, j + 1))

        for next_position in possible_next_positions:
            reachable_positions = TodaySolver.search_route(
                inp,
                next_value,
                next_position[0],
                next_position[1],
                W,
                H,
                reachable_positions,
            )

        return reachable_positions

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        W = len(inp[0])
        H = len(inp)

        inp = [[int(j) for j in i] for i in inp]

        starting_positions = []
        for i in range(H):
            for j in range(W):
                if inp[i][j] == 0:
                    starting_positions.append((i, j))

        result = 0
        for starting_position in starting_positions:
            reachable_positions = TodaySolver.search_route(
                inp, 0, starting_position[0], starting_position[1], W, H, set()
            )
            result += len(reachable_positions)

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
