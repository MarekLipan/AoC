"""
Solution for the day's puzzle
"""

import os
from typing import List
import numpy as np
from utils.solver import Solver

import logging
import sys

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler("debug.log")
handler.setLevel(logging.DEBUG)

# Create a stream handler to output to stdout
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)

# Create a logging format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(handler)
logger.addHandler(stream_handler)


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        pipe_map = []
        for line in inp:
            pipe_map.append(list(line))

        pipe_map = np.vstack(pipe_map)

        def single_move(prev_coords: tuple, current_coords: tuple) -> tuple:
            """Based on previous and current coordinates, return next coordinates"""

            current_symbol = pipe_map[current_coords[0], current_coords[1]]

            diff = (
                current_coords[0] - prev_coords[0],
                current_coords[1] - prev_coords[1],
            )
            if diff == (0, 1):
                inc_direction = "right"
            elif diff == (0, -1):
                inc_direction = "left"
            elif diff == (1, 0):
                inc_direction = "down"
            elif diff == (-1, 0):
                inc_direction = "up"

            if current_symbol == "|":
                if inc_direction == "down":
                    next_coords = (current_coords[0] + 1, current_coords[1])
                elif inc_direction == "up":
                    next_coords = (current_coords[0] - 1, current_coords[1])
            elif current_symbol == "-":
                if inc_direction == "right":
                    next_coords = (current_coords[0], current_coords[1] + 1)
                elif inc_direction == "left":
                    next_coords = (current_coords[0], current_coords[1] - 1)
            elif current_symbol == "L":
                if inc_direction == "down":
                    next_coords = (current_coords[0], current_coords[1] + 1)
                elif inc_direction == "left":
                    next_coords = (current_coords[0] - 1, current_coords[1])
            elif current_symbol == "J":
                if inc_direction == "down":
                    next_coords = (current_coords[0], current_coords[1] - 1)
                elif inc_direction == "right":
                    next_coords = (current_coords[0] - 1, current_coords[1])
            elif current_symbol == "7":
                if inc_direction == "right":
                    next_coords = (current_coords[0] + 1, current_coords[1])
                elif inc_direction == "up":
                    next_coords = (current_coords[0], current_coords[1] - 1)
            elif current_symbol == "F":
                if inc_direction == "up":
                    next_coords = (current_coords[0], current_coords[1] + 1)
                elif inc_direction == "left":
                    next_coords = (current_coords[0] + 1, current_coords[1])

            return current_coords, next_coords

        # single_move((0, 0), (0, 1))
        # find S
        start_coords = np.where(pipe_map == "S")
        start_coords = (start_coords[0][0], start_coords[1][0])

        prev_coords, next_coords = start_coords, (
            start_coords[0] + 1,  # custom modified based on my personal input
            start_coords[1],
        )

        output_map = np.full(pipe_map.shape, ".")
        output_map[start_coords[0], start_coords[1]] = "S"

        logger.debug("Starting first loop")

        while next_coords != start_coords:
            output_map[next_coords[0], next_coords[1]] = "x"
            prev_coords, next_coords = single_move(prev_coords, next_coords)

        # second round to fill in group A and group B points
        prev_coords, next_coords = start_coords, (
            start_coords[0] + 1,  # custom modified based on my personal input
            start_coords[1],
        )

        logger.debug("Starting second loop")

        while next_coords != start_coords:
            diff = (
                next_coords[0] - prev_coords[0],
                next_coords[1] - prev_coords[1],
            )
            if diff == (0, 1):
                inc_direction = "right"
            elif diff == (0, -1):
                inc_direction = "left"
            elif diff == (1, 0):
                inc_direction = "down"
            elif diff == (-1, 0):
                inc_direction = "up"

            next_symbol = pipe_map[next_coords[0], next_coords[1]]

            map_side_length = len(pipe_map)

            if next_symbol == "-":
                if (next_coords[0] - 1) >= 0 and output_map[
                    next_coords[0] - 1, next_coords[1]
                ] == ".":
                    if inc_direction == "right":
                        output_map[next_coords[0] - 1, next_coords[1]] = "A"
                    elif inc_direction == "left":
                        output_map[next_coords[0] - 1, next_coords[1]] = "B"
                if (next_coords[0] + 1) < map_side_length and output_map[
                    next_coords[0] + 1, next_coords[1]
                ] == ".":
                    if inc_direction == "right":
                        output_map[next_coords[0] + 1, next_coords[1]] = "B"
                    elif inc_direction == "left":
                        output_map[next_coords[0] + 1, next_coords[1]] = "A"
            elif next_symbol == "|":
                if (next_coords[1] - 1) >= 0 and output_map[
                    next_coords[0], next_coords[1] - 1
                ] == ".":
                    if inc_direction == "up":
                        output_map[next_coords[0], next_coords[1] - 1] = "A"
                    elif inc_direction == "down":
                        output_map[next_coords[0], next_coords[1] - 1] = "B"
                if (next_coords[1] + 1) < map_side_length and output_map[
                    next_coords[0], next_coords[1] + 1
                ] == ".":
                    if inc_direction == "up":
                        output_map[next_coords[0], next_coords[1] + 1] = "B"
                    elif inc_direction == "down":
                        output_map[next_coords[0], next_coords[1] + 1] = "A"
            elif next_symbol == "L":
                if (next_coords[1] - 1) >= 0 and output_map[
                    next_coords[0], next_coords[1] - 1
                ] == ".":
                    if inc_direction == "down":
                        output_map[next_coords[0], next_coords[1] - 1] = "B"
                    elif inc_direction == "left":
                        output_map[next_coords[0], next_coords[1] - 1] = "A"
                if (next_coords[0] + 1) < map_side_length and output_map[
                    next_coords[0] + 1, next_coords[1]
                ] == ".":
                    if inc_direction == "down":
                        output_map[next_coords[0] + 1, next_coords[1]] = "B"
                    elif inc_direction == "left":
                        output_map[next_coords[0] + 1, next_coords[1]] = "A"
            elif next_symbol == "J":
                if (next_coords[0] + 1) < map_side_length and output_map[
                    next_coords[0] + 1, next_coords[1]
                ] == ".":
                    if inc_direction == "right":
                        output_map[next_coords[0] + 1, next_coords[1]] = "B"
                    elif inc_direction == "down":
                        output_map[next_coords[0] + 1, next_coords[1]] = "A"
                if (next_coords[1] + 1) < map_side_length and output_map[
                    next_coords[0], next_coords[1] + 1
                ] == ".":
                    if inc_direction == "right":
                        output_map[next_coords[0], next_coords[1] + 1] = "B"
                    elif inc_direction == "down":
                        output_map[next_coords[0], next_coords[1] + 1] = "A"

            prev_coords, next_coords = single_move(prev_coords, next_coords)

        # growing the A and B groups until there is no more . to fill
        dot_set = np.argwhere(output_map == ".").tolist()
        A_set = np.argwhere(output_map == "A").tolist()
        B_set = np.argwhere(output_map == "B").tolist()

        update = True

        logger.debug("Starting third loop")

        while update:
            update = False
            for dot in dot_set:
                if (
                    ([dot[0] - 1, dot[1]] in A_set)
                    or ([dot[0] + 1, dot[1]] in A_set)
                    or ([dot[0], dot[1] - 1] in A_set)
                    or ([dot[0], dot[1] + 1] in A_set)
                ):
                    output_map[dot[0], dot[1]] = "A"
                    A_set.append(dot)
                    dot_set.remove(dot)
                    update = True
                elif (
                    ([dot[0] - 1, dot[1]] in B_set)
                    or ([dot[0] + 1, dot[1]] in B_set)
                    or ([dot[0], dot[1] - 1] in B_set)
                    or ([dot[0], dot[1] + 1] in B_set)
                ):
                    output_map[dot[0], dot[1]] = "B"
                    B_set.append(dot)
                    dot_set.remove(dot)
                    update = True

        # save output map as txt to the current directory of the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_dir, "output_map.txt")

        with open(output_path, "w") as f:
            for line in output_map:
                f.write("".join(line) + "\n")

        print(f"A: {len(A_set)}")
        print(f"B: {len(B_set)}")
        print(f".: {len(dot_set)}")

        return


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
