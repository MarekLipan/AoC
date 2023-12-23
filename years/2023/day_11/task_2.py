"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver

import numpy as np


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        expand_factor = 1000000

        universe = np.array([list(row) for row in inp])

        horizontal_expand_line_inds = []
        vertical_expand_line_inds = []

        for i in range(len(universe)):
            if np.all(universe[i, :] == "."):
                horizontal_expand_line_inds.append(i)
            if np.all(universe[:, i] == "."):
                vertical_expand_line_inds.append(i)

        # get coordinates of all galaxies
        galaxy_coordinates = np.where(np.array(universe) == "#")
        num_galaxies = len(galaxy_coordinates[0])

        # add all pair distances
        result = 0
        for i in range(num_galaxies):
            for j in range(i + 1, num_galaxies):
                vertical_start = min(galaxy_coordinates[0][i], galaxy_coordinates[0][j])
                vertical_end = max(galaxy_coordinates[0][i], galaxy_coordinates[0][j])
                horizontal_start = min(
                    galaxy_coordinates[1][i], galaxy_coordinates[1][j]
                )
                horizontal_end = max(galaxy_coordinates[1][i], galaxy_coordinates[1][j])

                result += (
                    vertical_end - vertical_start + horizontal_end - horizontal_start
                )

                # add distance for each expansion
                for h in horizontal_expand_line_inds:
                    if vertical_start <= h <= vertical_end:
                        result += expand_factor - 1
                for v in vertical_expand_line_inds:
                    if horizontal_start <= v <= horizontal_end:
                        result += expand_factor - 1

        # output_map = expanded_universe
        ## save output map as txt to the current directory of the script
        # script_dir = os.path.dirname(os.path.abspath(__file__))
        # output_path = os.path.join(script_dir, "output_map.txt")

        # with open(output_path, "w") as f:
        #    for line in output_map:
        #        f.write("".join(line) + "\n")

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
