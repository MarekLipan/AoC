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

        original_universe = [list(row) for row in inp]

        # vertically expand the universe
        vertically_expanded_universe = []
        for row in original_universe:
            vertically_expanded_universe.append(row)
            if np.all(np.array(row) == "."):
                vertically_expanded_universe.append(row)

        # transpose
        vertically_expanded_universe_T = np.array(
            vertically_expanded_universe
        ).T.tolist()

        # horizontally expand the universe
        horizontally_expanded_universe_T = []
        for row in vertically_expanded_universe_T:
            horizontally_expanded_universe_T.append(row)
            if np.all(np.array(row) == "."):
                horizontally_expanded_universe_T.append(row)

        # transpose back
        expanded_universe = np.array(horizontally_expanded_universe_T).T.tolist()

        # get coordinates of all galaxies
        galaxy_coordinates = np.where(np.array(expanded_universe) == "#")
        num_galaxies = len(galaxy_coordinates[0])

        # add all pair distances
        result = 0
        for i in range(num_galaxies):
            for j in range(i + 1, num_galaxies):
                result += abs(galaxy_coordinates[0][i] - galaxy_coordinates[0][j])
                result += abs(galaxy_coordinates[1][i] - galaxy_coordinates[1][j])

        output_map = expanded_universe
        # save output map as txt to the current directory of the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_dir, "output_map.txt")

        with open(output_path, "w") as f:
            for line in output_map:
                f.write("".join(line) + "\n")

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
