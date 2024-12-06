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

        import time

        start = time.time()

        W, H = len(inp[0]), len(inp)

        # find position of the guard
        for i in range(H):
            inp[i] = list(inp[i])
            for j in range(W):
                if inp[i][j] == "^":
                    starting_guard_position = (i, j)
                    break

        # find candidate positions for placing extra obstacles
        guard = starting_guard_position
        candidate_positions = set()
        active_direction = "up"

        while True:
            candidate_positions.add(guard)
            if active_direction == "up":
                if guard[0] - 1 < 0:
                    break

                if inp[guard[0] - 1][guard[1]] == "#":
                    active_direction = "right"
                else:
                    guard = (guard[0] - 1, guard[1])

            elif active_direction == "right":
                if guard[1] + 1 >= W:
                    break

                if inp[guard[0]][guard[1] + 1] == "#":
                    active_direction = "down"
                else:
                    guard = (guard[0], guard[1] + 1)

            elif active_direction == "down":
                if guard[0] + 1 >= H:
                    break

                if inp[guard[0] + 1][guard[1]] == "#":
                    active_direction = "left"
                else:
                    guard = (guard[0] + 1, guard[1])

            else:
                if guard[1] - 1 < 0:
                    break

                if inp[guard[0]][guard[1] - 1] == "#":
                    active_direction = "up"
                else:
                    guard = (guard[0], guard[1] - 1)

        # remove the starting guard position from the candidate positions
        candidate_positions.remove(starting_guard_position)

        # loop through all potential extra obstacle placements
        visited_position_direction = set()
        result = 0

        for i, j in candidate_positions:
            guard = starting_guard_position
            active_direction = "up"
            visited_position_direction = set()

            # place the extra obstacle
            inp[i][j] = "#"

            while True:
                visited_position_direction.add((guard[0], guard[1], active_direction))
                if active_direction == "up":
                    if guard[0] - 1 < 0:
                        break

                    if (guard[0] - 1, guard[1], "up") in visited_position_direction:
                        result += 1
                        break

                    if inp[guard[0] - 1][guard[1]] == "#":
                        active_direction = "right"
                    else:
                        guard = (guard[0] - 1, guard[1])

                elif active_direction == "right":
                    if guard[1] + 1 >= W:
                        break

                    if (
                        guard[0],
                        guard[1] + 1,
                        "right",
                    ) in visited_position_direction:
                        result += 1
                        break

                    if inp[guard[0]][guard[1] + 1] == "#":
                        active_direction = "down"
                    else:
                        guard = (guard[0], guard[1] + 1)

                elif active_direction == "down":
                    if guard[0] + 1 >= H:
                        break

                    if (
                        guard[0] + 1,
                        guard[1],
                        "down",
                    ) in visited_position_direction:
                        result += 1
                        break

                    if inp[guard[0] + 1][guard[1]] == "#":
                        active_direction = "left"
                    else:
                        guard = (guard[0] + 1, guard[1])

                else:
                    if guard[1] - 1 < 0:
                        break

                    if (
                        guard[0],
                        guard[1] - 1,
                        "left",
                    ) in visited_position_direction:
                        result += 1
                        break

                    if inp[guard[0]][guard[1] - 1] == "#":
                        active_direction = "up"
                    else:
                        guard = (guard[0], guard[1] - 1)

            # reset the extra obstacle
            inp[i][j] = "."

        end = time.time()
        print("Time taken:", end - start)

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
