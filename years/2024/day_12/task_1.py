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

        result = 0

        for p in plot_fences:
            assigned_nodes = [k for k, v in plot_assignments.items() if v == p]
            result += len(plot_fences[p]) * len(assigned_nodes)

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
