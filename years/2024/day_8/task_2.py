"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver
import itertools


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        W = len(inp[0])
        H = len(inp)

        antena_locations = {}
        for i in range(H):
            for j in range(W):
                if inp[i][j] != ".":
                    antena = inp[i][j]
                    if antena not in antena_locations:
                        antena_locations[antena] = []
                    antena_locations[antena].append((i, j))

        antinodes_locations = set()

        for antena, locations in antena_locations.items():
            # loop through all pairs of locations
            combinations = list(itertools.permutations(locations, 2))

            for a, b in combinations:
                y_diff = b[0] - a[0]
                x_diff = b[1] - a[1]

                # all possible antinode locations in the grid
                in_grid = True
                antinode_a = a
                while in_grid:
                    antinodes_locations.add(antinode_a)
                    antinode_a = (antinode_a[0] - y_diff, antinode_a[1] - x_diff)
                    if not (0 <= antinode_a[0] < H and 0 <= antinode_a[1] < W):
                        in_grid = False

                in_grid = True
                antinode_b = b
                while in_grid:
                    antinodes_locations.add(antinode_b)
                    antinode_b = (antinode_b[0] + y_diff, antinode_b[1] + x_diff)
                    if not (0 <= antinode_b[0] < H and 0 <= antinode_b[1] < W):
                        in_grid = False

        return len(antinodes_locations)


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
