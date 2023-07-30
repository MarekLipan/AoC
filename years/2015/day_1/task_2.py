"""
Solution for the day's puzzle
"""

import os
from typing import List


def solution(inp: List[str]):
    """
    Solution for the day's puzzle
    """

    instructions = inp[0]

    floor = 0
    i = 0

    while floor != -1:
        if instructions[i] == "(":
            floor += 1
        elif instructions[i] == ")":
            floor -= 1

        i += 1

    return i


def main():
    """
    Function to solve the puzzle
    """

    with open(
        os.path.join(os.path.realpath(__file__), "../test_input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        task_test_input = input_file.readlines()

    with open(
        os.path.join(os.path.realpath(__file__), "../input.txt"),
        "r",
        encoding="utf-8",
    ) as input_file:
        task_input = input_file.readlines()

    print(f"Test input Solution: {solution(task_test_input)}")
    print(f"Solution: {solution(task_input)}")


if __name__ == "__main__":
    main()
