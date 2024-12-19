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

    @staticmethod
    def search_for_neighbor_nodes(
        inp, n, H, W, unassigned_nodes, plot_assignments, plot_fences
    ):
        """Search for neighbors of a node with same value. Assigns the same plot id to them"""
        # add plot fences (y1, x1, y2, x2)
        fence_candidates = [
            (n[0], n[1], n[0] + 1, n[1]),  # left side
            (n[0], n[1], n[0], n[1] + 1),  # top side
            (n[0] + 1, n[1], n[0] + 1, n[1] + 1),  # bottom side
            (n[0], n[1] + 1, n[0] + 1, n[1] + 1),  # right side
        ]
        for fc in fence_candidates:
            # add fence if it is not already added
            if fc not in plot_fences[plot_assignments[n]]:
                plot_fences[plot_assignments[n]].add(fc)
            # remove fence if it is already added in this plot
            else:
                plot_fences[plot_assignments[n]].remove(fc)

        next_nodes = []
        if n[0] > 0:
            next_nodes.append((n[0] - 1, n[1]))
        if n[0] < H - 1:
            next_nodes.append((n[0] + 1, n[1]))
        if n[1] > 0:
            next_nodes.append((n[0], n[1] - 1))
        if n[1] < W - 1:
            next_nodes.append((n[0], n[1] + 1))

        neighbor_nodes = []
        for next_n in next_nodes:
            if inp[next_n[0]][next_n[1]] == inp[n[0]][n[1]]:
                neighbor_nodes.append(next_n)

        for nb_n in neighbor_nodes:
            if nb_n in unassigned_nodes:
                unassigned_nodes.remove(nb_n)
                plot_assignments[nb_n] = plot_assignments[n]

                plot_assignments, plot_fences = TodaySolver.search_for_neighbor_nodes(
                    inp, nb_n, H, W, unassigned_nodes, plot_assignments, plot_fences
                )

        return plot_assignments, plot_fences

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        H = len(inp)
        W = len(inp[0])

        unassigned_nodes = set(list(itertools.product(range(H), range(W))))
        plot_id = 0
        plot_assignments = {}
        plot_fences = {}

        while unassigned_nodes:
            n = unassigned_nodes.pop()
            plot_assignments[n] = plot_id
            plot_fences[plot_id] = set()

            plot_assignments, plot_fences = TodaySolver.search_for_neighbor_nodes(
                inp, n, H, W, unassigned_nodes, plot_assignments, plot_fences
            )

            plot_id += 1

        plot_sides = {}
        for p, fences in plot_fences.items():
            checked_fences = set()
            sides = len(plot_fences[p])

            print(f"Plot {p} has {sides} sides")

            for f in fences:
                # is it a horizontal or vertical fence?
                if f[0] == f[2]:
                    # horizontal fence
                    # value above and below
                    if f[0] > 0:
                        top_value = inp[f[0] - 1][f[1]]
                    else:
                        top_value = None
                    if f[0] < H:
                        bottom_value = inp[f[0]][f[1]]
                    else:
                        bottom_value = None
                    # is there a connection on the left or right side?
                    left_fence = (f[0], f[1] - 1, f[2], f[3] - 1)
                    right_fence = (f[0], f[1] + 1, f[2], f[3] + 1)
                    if left_fence in checked_fences:
                        if top_value is not None and bottom_value is not None:
                            if (top_value == inp[f[0] - 1][f[1] - 1]) or (
                                bottom_value == inp[f[0]][f[1] - 1]
                            ):
                                sides -= 1
                        else:
                            sides -= 1
                    if right_fence in checked_fences:
                        if top_value is not None and bottom_value is not None:
                            if (top_value == inp[f[0] - 1][f[1] + 1]) or (
                                bottom_value == inp[f[0]][f[1] + 1]
                            ):
                                sides -= 1
                        else:
                            sides -= 1
                else:
                    # vertical fence
                    # value on the left and right
                    if f[1] > 0:
                        left_value = inp[f[0]][f[1] - 1]
                    else:
                        left_value = None
                    if f[1] < W:
                        right_value = inp[f[0]][f[1]]
                    else:
                        right_value = None
                    # is there a connection on the top or bottom side?
                    top_fence = (f[0] - 1, f[1], f[2] - 1, f[3])
                    bottom_fence = (f[0] + 1, f[1], f[2] + 1, f[3])
                    if top_fence in checked_fences:
                        if left_value is not None and right_value is not None:
                            if (left_value == inp[f[0] - 1][f[1] - 1]) or (
                                right_value == inp[f[0] - 1][f[1]]
                            ):
                                sides -= 1
                        else:
                            sides -= 1
                    if bottom_fence in checked_fences:
                        if left_value is not None and right_value is not None:
                            if (left_value == inp[f[0] + 1][f[1] - 1]) or (
                                right_value == inp[f[0] + 1][f[1]]
                            ):
                                sides -= 1
                        else:
                            sides -= 1

                print(f"Adding fence {f} to checked fences. Sides: {sides}")
                checked_fences.add(f)

            print(f"Plot {p} has {sides} sides after checking")

            plot_sides[p] = sides

        result = 0
        for p, s in plot_sides.items():
            assigned_nodes = [k for k, v in plot_assignments.items() if v == p]
            result += s * len(assigned_nodes)

            print(
                f"Plot value {inp[assigned_nodes[0][0]][assigned_nodes[0][1]]} has area {len(assigned_nodes)} and {s} sides, adding {s * len(assigned_nodes)}"
            )

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
