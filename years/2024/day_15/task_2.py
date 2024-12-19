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
        original_field = field[:gap]

        # enlarge the field
        field = []
        for row in original_field:
            new_row = []
            for j in row:
                if j == "#":
                    new_row.append("#")
                    new_row.append("#")
                elif j == "O":
                    new_row.append("[")
                    new_row.append("]")
                elif j == ".":
                    new_row.append(".")
                    new_row.append(".")
                elif j == "@":
                    new_row.append("@")
                    new_row.append(".")
            field.append(new_row)

        # find starting position
        for i, row in enumerate(field):
            if "@" in row:
                position = (i, row.index("@"))
                break
        field[position[0]][position[1]] = "."  # field is now clear

        # shorten the instruction list for DEBUGGING
        # instruction = instruction[:191]
        # print(f"Instruction: {instruction}")

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
                    while field[neighbour_position[0]][neighbour_position[1]] in [
                        "[",
                        "]",
                    ]:
                        neighbour_position = (
                            neighbour_position[0],
                            neighbour_position[1] + 1,
                        )
                    if field[neighbour_position[0]][neighbour_position[1]] == "#":
                        continue
                    else:
                        # move the stones
                        field[position[0]][
                            position[1] + 2 : neighbour_position[1] + 1
                        ] = field[position[0]][position[1] + 1 : neighbour_position[1]]
                        # move the position
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
                    while field[neighbour_position[0]][neighbour_position[1]] in [
                        "[",
                        "]",
                    ]:
                        neighbour_position = (
                            neighbour_position[0],
                            neighbour_position[1] - 1,
                        )
                    if field[neighbour_position[0]][neighbour_position[1]] == "#":
                        continue
                    else:
                        # move the stones
                        field[position[0]][neighbour_position[1] : position[1] - 1] = (
                            field[position[0]][neighbour_position[1] + 1 : position[1]]
                        )
                        # move the position
                        position = (position[0], position[1] - 1)
                        # clear the position
                        field[position[0]][position[1]] = "."

            elif next_move == "^":
                if field[position[0] - 1][position[1]] == ".":
                    position = (position[0] - 1, position[1])
                elif field[position[0] - 1][position[1]] == "#":
                    continue
                else:
                    # try to move the stones upwards
                    # first figure out what is in the stack of stones to be moved upwards
                    stone_stack = {}
                    level = position[0]
                    if field[level - 1][position[1]] == "[":
                        stone_stack[level - 1] = [(position[1], position[1] + 1)]
                    else:
                        stone_stack[level - 1] = [(position[1] - 1, position[1])]

                    hit_wall = False
                    while stone_stack[level - 1]:
                        level -= 1
                        stone_stack[level - 1] = []

                        for s in stone_stack[level]:
                            if (
                                field[level - 1][s[0]] == "#"
                                or field[level - 1][s[1]] == "#"
                            ):
                                hit_wall = True
                                break
                            if (
                                field[level - 1][s[0]] == "["
                                and field[level - 1][s[1]] == "]"
                            ):
                                stone_stack[level - 1].append((s[0], s[1]))
                            elif (
                                field[level - 1][s[0]] == "]"
                                and field[level - 1][s[1]] == "."
                            ):
                                stone_stack[level - 1].append((s[0] - 1, s[0]))
                            elif (
                                field[level - 1][s[0]] == "."
                                and field[level - 1][s[1]] == "["
                            ):
                                stone_stack[level - 1].append((s[1], s[1] + 1))
                            elif (
                                field[level - 1][s[0]] == "]"
                                and field[level - 1][s[1]] == "["
                            ):
                                stone_stack[level - 1].append((s[0] - 1, s[0]))
                                stone_stack[level - 1].append((s[1], s[1] + 1))

                    if hit_wall:
                        continue

                    # move the stones
                    for l in range(level, position[0]):
                        for s in stone_stack[l]:
                            # move the stone upwards
                            field[l - 1][s[0]] = "["
                            field[l - 1][s[1]] = "]"
                            # clear after the stone
                            field[l][s[0]] = "."
                            field[l][s[1]] = "."

                    # move the position
                    position = (position[0] - 1, position[1])

            elif next_move == "v":
                if field[position[0] + 1][position[1]] == ".":
                    position = (position[0] + 1, position[1])
                elif field[position[0] + 1][position[1]] == "#":
                    continue
                else:
                    # try to move the stones downwards
                    # first figure out what is in the stack of stones to be moved downwards
                    stone_stack = {}
                    level = position[0]
                    if field[level + 1][position[1]] == "[":
                        stone_stack[level + 1] = [(position[1], position[1] + 1)]
                    else:
                        stone_stack[level + 1] = [(position[1] - 1, position[1])]

                    hit_wall = False
                    while stone_stack[level + 1]:
                        level += 1
                        stone_stack[level + 1] = []

                        for s in stone_stack[level]:
                            if (
                                field[level + 1][s[0]] == "#"
                                or field[level + 1][s[1]] == "#"
                            ):
                                hit_wall = True
                                break
                            if (
                                field[level + 1][s[0]] == "["
                                and field[level + 1][s[1]] == "]"
                            ):
                                stone_stack[level + 1].append((s[0], s[1]))
                            elif (
                                field[level + 1][s[0]] == "]"
                                and field[level + 1][s[1]] == "."
                            ):
                                stone_stack[level + 1].append((s[0] - 1, s[0]))
                            elif (
                                field[level + 1][s[0]] == "."
                                and field[level + 1][s[1]] == "["
                            ):
                                stone_stack[level + 1].append((s[1], s[1] + 1))
                            elif (
                                field[level + 1][s[0]] == "]"
                                and field[level + 1][s[1]] == "["
                            ):
                                stone_stack[level + 1].append((s[0] - 1, s[0]))
                                stone_stack[level + 1].append((s[1], s[1] + 1))

                    if hit_wall:
                        continue

                    # move the stones
                    for l in range(level, position[0], -1):
                        for s in stone_stack[l]:
                            # move the stone downwards
                            field[l + 1][s[0]] = "["
                            field[l + 1][s[1]] = "]"
                            # clear after the stone
                            field[l][s[0]] = "."
                            field[l][s[1]] = "."

                    # move the position
                    position = (position[0] + 1, position[1])

        result = 0
        num_stone = 0

        for i in range(len(field)):
            for j in range(len(field[0])):
                if field[i][j] == "[":
                    result += 100 * i + j

                    num_stone += 1

        print(num_stone)

        with open(
            "/Users/marek.lipan/Desktop/Projects/AoC/years/2024/day_15/task_2_debug.txt",
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
