# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/12

from ...base import StrSplitSolution, answer
from typing import Dict, List, NamedTuple, Union
from dataclasses import dataclass
from enum import Enum, auto

class Solution(StrSplitSolution):
    _year = 2016
    _day = 12

    class Operation(Enum):
        CPY = auto()
        INC = auto()
        DEC = auto()
        JNZ = auto()

    class Instruction(NamedTuple):
        op: "Solution.Operation"
        lhs: int | str
        rhs: int | str

    @staticmethod
    def parse_input(input: list[str]) -> list[Instruction]:
        op_map = {
            "cpy": Solution.Operation.CPY,
            "inc": Solution.Operation.INC,
            "dec": Solution.Operation.DEC,
            "jnz": Solution.Operation.JNZ,
        }
        insns = []
        for l in input:
            l = l.split()
            op = op_map[l[0]]
            if op == Solution.Operation.CPY or op == Solution.Operation.JNZ:
                lhs = int(l[1]) if not l[1] in {'a', 'b', 'c', 'd'} else l[1]
                rhs = int(l[2]) if not l[2] in {'a', 'b', 'c', 'd'} else l[2]
                insns.append(Solution.Instruction(op, lhs, rhs))
            else:
                insns.append(Solution.Instruction(op, l[1], 0))
        return insns

    @dataclass
    class Puzzle:
        instructions: list["Solution.Instruction"]
        regs: dict[str, int]

        def solve(self) -> int:
            i = 0
            while i < len(self.instructions):
                ins = self.instructions[i]
                op, lhs, rhs = ins
                match op:
                    case Solution.Operation.CPY:
                        self.regs[rhs] = lhs if isinstance(lhs, int) else self.regs[lhs]
                    case Solution.Operation.INC:
                        self.regs[lhs] += 1
                    case Solution.Operation.DEC:
                        self.regs[lhs] -= 1
                    case Solution.Operation.JNZ:
                        lhs = lhs if isinstance(lhs, int) else self.regs[lhs]
                        rhs = rhs if isinstance(rhs, int) else self.regs[rhs]
                        if lhs != 0:
                            i += rhs - 1
                i += 1
            return self.regs["a"]

    # @answer(1234)
    def part_1(self) -> int:
        instructions: List[Solution.Instruction] = Solution.parse_input(self.input)
        regs: Dict[str, int] = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
        }
        return Solution.Puzzle(instructions, regs).solve()

    # @answer(1234)
    def part_2(self) -> int:
        instructions: List[Solution.Instruction] = Solution.parse_input(self.input)
        regs: Dict[str, int] = {
            'a': 0,
            'b': 0,
            'c': 1,
            'd': 0,
        }
        return Solution.Puzzle(instructions, regs).solve()

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
