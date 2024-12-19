"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver
from typing import Union
import sys


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    @staticmethod
    def step_in_maze(
        maze: List[str],
        position: tuple,
        current_direction: str,
        end: tuple,
        current_score: int,
        lowest_score: Union[int, None],
        path: List[tuple],
        best_paths_nodes: set,
        maze_costs: dict,
    ):
        """Recursive function to step in the maze and find path with lowest score"""
        path = path + [position]
        # note the positions on the best paths
        if position == end and current_score == 88416:
            for p in path:
                best_paths_nodes.add(p)
        # stop if this position and direction was reached with lower score already
        if maze_costs[current_direction].get(position, 100000) < current_score:
            return lowest_score
        maze_costs[current_direction][position] = current_score
        # stop if the current score is higher than the lowest score because lowest score can be reached
        if lowest_score is not None and current_score > lowest_score:
            return lowest_score

        # stop if the end is reached
        if position == end:
            if lowest_score is None:
                lowest_score = current_score
            else:
                lowest_score = min(lowest_score, current_score)
            return lowest_score

        # find possible next directions
        possible_directions = []
        if maze[position[0] - 1][position[1]] != "#" and current_direction != "down":
            possible_directions.append("up")
        if maze[position[0] + 1][position[1]] != "#" and current_direction != "up":
            possible_directions.append("down")
        if maze[position[0]][position[1] - 1] != "#" and current_direction != "right":
            possible_directions.append("left")
        if maze[position[0]][position[1] + 1] != "#" and current_direction != "left":
            possible_directions.append("right")

        for direction in possible_directions:
            current_score += 1 + (current_direction != direction) * 1000
            lowest_score = TodaySolver.step_in_maze(
                maze,
                (
                    position[0] + (direction == "down") - (direction == "up"),
                    position[1] + (direction == "right") - (direction == "left"),
                ),
                direction,
                end,
                current_score,
                lowest_score,
                path,
                best_paths_nodes,
                maze_costs,
            )
            current_score -= 1 + (current_direction != direction) * 1000

        return lowest_score

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""
        maze = [list(row) for row in inp]
        # find the start and end tiles
        start = (-1, -1)
        end = (-1, -1)
        for i, line in enumerate(maze):
            if "S" in line:
                start = (i, line.index("S"))
            if "E" in line:
                end = (i, line.index("E"))

        direction = "right"

        lowest_score = None
        current_score = 0
        path = []
        best_paths_nodes = set()
        maze_costs = {"right": {}, "left": {}, "up": {}, "down": {}}
        lowest_score = self.step_in_maze(
            maze,
            start,
            direction,
            end,
            current_score,
            100000,
            path,
            best_paths_nodes,
            maze_costs,
        )

        print(len(best_paths_nodes))

        with open(
            "/Users/marek.lipan/Desktop/Projects/AoC/years/2024/day_16/task_2_debug.txt",
            "w",
            encoding="utf-8",
        ) as f:
            for i in range(len(maze)):
                for j in range(len(maze[i])):
                    if (i, j) in best_paths_nodes:
                        f.write("O")
                    elif maze[i][j] == "#":
                        f.write("#")
                    else:
                        f.write(".")
                f.write("\n")

        return lowest_score


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
