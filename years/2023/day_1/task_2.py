"""
Solution for the day's puzzle
"""


import sys

sys.path.append("/Users/marek.lipan/Desktop/Projects/AoC")


import os
from typing import List
from utils.solver import Solver


class TodaySolver(Solver):
    """
    Contains input and solution for today
    """

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        def _turn_word_numbers_into_digits(line: str, forward: bool = True):
            update = True
            if forward:
                while update:
                    update = False
                    for i, _ in enumerate(line):
                        if i >= 2 and line[i - 2 : i + 1] == "one":
                            line = line[: i - 2] + "1" + line[i + 1 :]
                            update = True
                            break
                        if i >= 2 and line[i - 2 : i + 1] == "six":
                            line = line[: i - 2] + "6" + line[i + 1 :]
                            update = True
                            break
                        if i >= 2 and line[i - 2 : i + 1] == "two":
                            line = line[: i - 2] + "2" + line[i + 1 :]
                            update = True
                            break
                        if i >= 3 and line[i - 3 : i + 1] == "four":
                            line = line[: i - 3] + "4" + line[i + 1 :]
                            update = True
                            break
                        if i >= 3 and line[i - 3 : i + 1] == "five":
                            line = line[: i - 3] + "5" + line[i + 1 :]
                            update = True
                            break
                        if i >= 3 and line[i - 3 : i + 1] == "nine":
                            line = line[: i - 3] + "9" + line[i + 1 :]
                            update = True
                            break
                        if i >= 4 and line[i - 4 : i + 1] == "three":
                            line = line[: i - 4] + "3" + line[i + 1 :]
                            update = True
                            break
                        if i >= 4 and line[i - 4 : i + 1] == "seven":
                            line = line[: i - 4] + "7" + line[i + 1 :]
                            update = True
                            break
                        if i >= 4 and line[i - 4 : i + 1] == "eight":
                            line = line[: i - 4] + "8" + line[i + 1 :]
                            update = True
                            break
            else:
                while update:
                    update = False
                    for i, _ in enumerate(line):
                        if i >= 2 and line[i - 2 : i + 1] == "eno":
                            line = line[: i - 2] + "1" + line[i + 1 :]
                            update = True
                            break
                        if i >= 2 and line[i - 2 : i + 1] == "xis":
                            line = line[: i - 2] + "6" + line[i + 1 :]
                            update = True
                            break
                        if i >= 2 and line[i - 2 : i + 1] == "owt":
                            line = line[: i - 2] + "2" + line[i + 1 :]
                            update = True
                            break
                        if i >= 3 and line[i - 3 : i + 1] == "ruof":
                            line = line[: i - 3] + "4" + line[i + 1 :]
                            update = True
                            break
                        if i >= 3 and line[i - 3 : i + 1] == "evif":
                            line = line[: i - 3] + "5" + line[i + 1 :]
                            update = True
                            break
                        if i >= 3 and line[i - 3 : i + 1] == "enin":
                            line = line[: i - 3] + "9" + line[i + 1 :]
                            update = True
                            break
                        if i >= 4 and line[i - 4 : i + 1] == "eerht":
                            line = line[: i - 4] + "3" + line[i + 1 :]
                            update = True
                            break
                        if i >= 4 and line[i - 4 : i + 1] == "neves":
                            line = line[: i - 4] + "7" + line[i + 1 :]
                            update = True
                            break
                        if i >= 4 and line[i - 4 : i + 1] == "thgie":
                            line = line[: i - 4] + "8" + line[i + 1 :]
                            update = True
                            break

            return line

        result = 0
        for line in inp:
            transformed_line = _turn_word_numbers_into_digits(line, forward=True)
            transformed_line_backwards = _turn_word_numbers_into_digits(
                line[::-1], forward=False
            )
            # first number
            for i in transformed_line:
                if i.isdigit():
                    first_num = i
                    break
            # second number
            for i in transformed_line_backwards:
                if i.isdigit():
                    second_num = i
                    break

            print(
                f"{line} : {transformed_line} : {transformed_line_backwards} : {int(first_num + second_num)}"
            )

            result += int(first_num + second_num)

        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=True)
