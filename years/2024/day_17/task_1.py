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

    @staticmethod
    def combo_operand(operand: int, register: dict):
        if operand in [1, 2, 3]:
            return operand
        if operand == 4:
            return register["A"]
        if operand == 5:
            return register["B"]
        if operand == 6:
            return register["C"]

    @staticmethod
    def adv(
        operand: int, register: dict, output: list, pointer: int, jump: bool = False
    ):
        register["A"] = register["A"] // (
            2 ** TodaySolver.combo_operand(operand, register)
        )
        return register, output, pointer, jump

    @staticmethod
    def bxl(
        operand: int, register: dict, output: list, pointer: int, jump: bool = False
    ):
        register["B"] = register["B"] ^ operand
        return register, output, pointer, jump

    @staticmethod
    def bst(
        operand: int, register: dict, output: list, pointer: int, jump: bool = False
    ):
        register["B"] = TodaySolver.combo_operand(operand, register) % 8
        return register, output, pointer, jump

    @staticmethod
    def jnz(
        operand: int, register: dict, output: list, pointer: int, jump: bool = False
    ):
        if register["A"] == 0:
            return register, output, pointer, jump

        jump = True
        pointer = operand

        return register, output, pointer, jump

    @staticmethod
    def bxc(
        operand: int, register: dict, output: list, pointer: int, jump: bool = False
    ):
        register["B"] = register["B"] ^ register["C"]
        return register, output, pointer, jump

    @staticmethod
    def out(
        operand: int, register: dict, output: list, pointer: int, jump: bool = False
    ):
        output.append(TodaySolver.combo_operand(operand, register) % 8)
        return register, output, pointer, jump

    @staticmethod
    def bdv(
        operand: int, register: dict, output: list, pointer: int, jump: bool = False
    ):
        register["B"] = register["A"] // (
            2 ** TodaySolver.combo_operand(operand, register)
        )
        return register, output, pointer, jump

    @staticmethod
    def cdv(
        operand: int, register: dict, output: list, pointer: int, jump: bool = False
    ):
        register["C"] = register["A"] // (
            2 ** TodaySolver.combo_operand(operand, register)
        )
        return register, output, pointer, jump

    def solution(self, inp: List[str]):
        """Placeholder for the solution function"""

        A = int(re.findall("(\d+)", inp[0])[0])
        B = int(re.findall("(\d+)", inp[1])[0])
        C = int(re.findall("(\d+)", inp[2])[0])
        program = list(map(int, re.findall("(\d+)", inp[4])))

        register = {"A": A, "B": B, "C": C}

        print(register)
        print(program)

        pointer = 0
        output = []

        while pointer < len(program):
            instruction = program[pointer]
            operand = program[pointer + 1]

            if instruction == 0:
                register, output, pointer, jump = TodaySolver.adv(
                    operand, register, output, pointer
                )
            elif instruction == 1:
                register, output, pointer, jump = TodaySolver.bxl(
                    operand, register, output, pointer
                )
            elif instruction == 2:
                register, output, pointer, jump = TodaySolver.bst(
                    operand, register, output, pointer
                )
            elif instruction == 3:
                register, output, pointer, jump = TodaySolver.jnz(
                    operand, register, output, pointer
                )
            elif instruction == 4:
                register, output, pointer, jump = TodaySolver.bxc(
                    operand, register, output, pointer
                )
            elif instruction == 5:
                register, output, pointer, jump = TodaySolver.out(
                    operand, register, output, pointer
                )
            elif instruction == 6:
                register, output, pointer, jump = TodaySolver.bdv(
                    operand, register, output, pointer
                )
            else:
                register, output, pointer, jump = TodaySolver.cdv(
                    operand, register, output, pointer
                )

            if not jump:
                pointer += 2

        result = ",".join(str(num) for num in output)
        return result


today_solver = TodaySolver(os.path.realpath(__file__))
today_solver.solve_and_print_result(solve_main_task=False)
