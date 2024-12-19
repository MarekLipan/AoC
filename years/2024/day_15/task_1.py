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

        field = [list(row) for row in inp]

        gap = field.index([])

        instructions = field[gap + 1 :]
        # join the instruction lists to a single list
        instruction = [item for sublist in instructions for item in sublist]
        field = field[:gap]

        # find starting position
        for i, row in enumerate(field):
            if "@" in row:
                position = (i, row.index("@"))
                break
        field[position[0]][position[1]] = "."  # field is now clear

        while instruction:
            next_move = instruction.pop(0)

            if next_move == ">":
                if field[position[0]][position[1] + 1] == ".":
                    position = (position[0], position[1] + 1)
                elif field[position[0]][position[1] + 1] == "#":
                    continue
                else:
                    # try to move the stones
                    neighbour_position = (position[0], position[1] + 1)
                    while field[neighbour_position[0]][neighbour_position[1]] == "O":
                        neighbour_position = (
                            neighbour_position[0],
                            neighbour_position[1] + 1,
                        )
                    if field[neighbour_position[0]][neighbour_position[1]] == "#":
                        continue
                    else:
                        # move the stones
                        for i in range(position[1] + 2, neighbour_position[1] + 1):
                            field[neighbour_position[0]][i] = "O"
                        position = (position[0], position[1] + 1)
                        # clear the position
                        field[position[0]][position[1]] = "."

            elif next_move == "<":
                if field[position[0]][position[1] - 1] == ".":
                    position = (position[0], position[1] - 1)
                elif field[position[0]][position[1] - 1] == "#":
                    continue
                else:
                    # try to move the stones
                    neighbour_position = (position[0], position[1] - 1)
                    while field[neighbour_position[0]][neighbour_position[1]] == "O":
                        neighbour_position = (
                            neighbour_position[0],
                            neighbour_position[1] - 1,
                        )
                    if field[neighbour_position[0]][neighbour_position[1]] == "#":
                        continue
                    else:
                        # move the stones
                        for i in range(neighbour_position[1], position[1] - 1):
                            field[neighbour_position[0]][i] = "O"
                        position = (position[0], position[1] - 1)
                        # clear the position
                        field[position[0]][position[1]] = "."

            elif next_move == "^":
                if field[position[0] - 1][position[1]] == ".":
                    position = (position[0] - 1, position[1])
                elif field[position[0] - 1][position[1]] == "#":
                    continue
                else:
                    # try to move the stones
                    neighbour_position = (position[0] - 1, position[1])
                    while field[neighbour_position[0]][neighbour_position[1]] == "O":
                        neighbour_position = (
                            neighbour_position[0] - 1,
                            neighbour_position[1],
                        )
                    if field[neighbour_position[0]][neighbour_position[1]] == "#":
                        continue
                    else:
                        # move the stones
                        for i in range(neighbour_position[0], position[0] - 1):
                            field[i][neighbour_position[1]] = "O"
                        position = (position[0] - 1, position[1])
                        # clear the position
                        field[position[0]][position[1]] = "."

            elif next_move == "v":
                if field[position[0] + 1][position[1]] == ".":
                    position = (position[0] + 1, position[1])
                elif field[position[0] + 1][position[1]] == "#":
                    continue
                else:
                    # try to move the stones
                    neighbour_position = (position[0] + 1, position[1])
                    while field[neighbour_position[0]][neighbour_position[1]] == "O":
                        neighbour_position = (
                            neighbour_position[0] + 1,
                            neighbour_position[1],
                        )
                    if field[neighbour_position[0]][neighbour_position[1]] == "#":
                        continue
                    else:
                        # move the stones
                        for i in range(position[0] + 2, neighbour_position[0] + 1):
                            field[i][neighbour_position[1]] = "O"
                        position = (position[0] + 1, position[1])
                        # clear the position
                        field[position[0]][position[1]] = "."

        result = 0

        for i in range(len(field)):
            for j in range(len(field[0])):
                if field[i][j] == "O":
                    result += 100 * i + j

        with open(
            "/Users/marek.lipan/Desktop/Projects/AoC/years/2024/day_15/task_1_debug.txt",
            "w",
            encoding="utf-8",
        ) as f:
            for i in range(len(field)):
                for j in range(len(field[0])):
                    if (i, j) == position:
                        f.write("@")
                    else:
                        f.write(field[i][j])
                f.write("\n")

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
