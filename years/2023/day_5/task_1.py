"""
Solution for the day's puzzle
"""

import os
from typing import List
from utils.solver import Solver
import re


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        # parsing the input
        seeds = [int(i) for i in re.findall("(\d+)", inp[0])]

        s2s = []
        s2f = []
        f2w = []
        w2l = []
        l2t = []
        t2h = []
        h2l = []

        active_map = None

        for l in inp:
            if l == "":
                active_map = None

            if active_map == "s2s":
                s2s.append([int(i) for i in re.findall("(\d+)", l)])
            elif active_map == "s2f":
                s2f.append([int(i) for i in re.findall("(\d+)", l)])
            elif active_map == "f2w":
                f2w.append([int(i) for i in re.findall("(\d+)", l)])
            elif active_map == "w2l":
                w2l.append([int(i) for i in re.findall("(\d+)", l)])
            elif active_map == "l2t":
                l2t.append([int(i) for i in re.findall("(\d+)", l)])
            elif active_map == "t2h":
                t2h.append([int(i) for i in re.findall("(\d+)", l)])
            elif active_map == "h2l":
                h2l.append([int(i) for i in re.findall("(\d+)", l)])

            if l == "seed-to-soil map:":
                active_map = "s2s"
            elif l == "soil-to-fertilizer map:":
                active_map = "s2f"
            elif l == "fertilizer-to-water map:":
                active_map = "f2w"
            elif l == "water-to-light map:":
                active_map = "w2l"
            elif l == "light-to-temperature map:":
                active_map = "l2t"
            elif l == "temperature-to-humidity map:":
                active_map = "t2h"
            elif l == "humidity-to-location map:":
                active_map = "h2l"

        def single_pass(map: list[list[int]], i: int) -> int:
            for m in map:
                diff = i - m[1]
                if 0 <= diff <= m[2]:
                    return m[0] + diff
            return i

        def seed_pass(seed: int) -> int:
            soil = single_pass(s2s, seed)
            fertilizer = single_pass(s2f, soil)
            water = single_pass(f2w, fertilizer)
            light = single_pass(w2l, water)
            temperature = single_pass(l2t, light)
            humidity = single_pass(t2h, temperature)
            location = single_pass(h2l, humidity)

            return location

        locations = []

        for seed in seeds:
            locations.append(seed_pass(seed))

        return min(locations)


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
