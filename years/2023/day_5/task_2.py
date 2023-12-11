"""
Solution for the day's puzzle
"""

import os
from typing import List
import re

from utils.solver import Solver


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

        def single_backwards_pass(map: list[list[int]], i: int) -> int:
            for m in map:
                diff = i - m[0]
                if 0 <= diff <= m[2]:
                    return m[1] + diff
            return i

        def location_pass(location: int) -> int:
            humidity = single_backwards_pass(h2l, location)
            temperature = single_backwards_pass(t2h, humidity)
            light = single_backwards_pass(l2t, temperature)
            water = single_backwards_pass(w2l, light)
            fertilizer = single_backwards_pass(f2w, water)
            soil = single_backwards_pass(s2f, fertilizer)
            seed = single_backwards_pass(s2s, soil)

            return seed

        # for s in tqdm.tqdm(range(0, len(seeds), 2)):
        #    for seed in range(seeds[s], seeds[s] + seeds[s + 1]):
        #        locations.append(seed_pass(seed))

        location = 0
        while True:
            seed = location_pass(location)

            # check if we have this seed
            for s in range(0, len(seeds), 2):
                if seeds[s] <= seed < seeds[s] + seeds[s + 1]:
                    return location

            location += 1


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
