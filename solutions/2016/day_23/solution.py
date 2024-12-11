# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/23

from ...base import StrSplitSolution, answer
from typing import Dict, List
from dataclasses import dataclass
from enum import Enum, auto
import copy

class Solution(StrSplitSolution):
    _year = 2016
    _day = 23

    class Operation(Enum):
        CPY = auto()
        INC = auto()
        DEC = auto()
        JNZ = auto()
        TGL = auto()

    @dataclass
    class Instruction:
        op: "Solution.Operation"
        lhs: int | str
        rhs: int | str | None

    @staticmethod
    def parse_input(input: list[str]) -> list[Instruction]:
        op_map = {
            "cpy": Solution.Operation.CPY,
            "inc": Solution.Operation.INC,
            "dec": Solution.Operation.DEC,
            "jnz": Solution.Operation.JNZ,
            "tgl": Solution.Operation.TGL,
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
                insns.append(Solution.Instruction(op, l[1], None))
        return insns

    @dataclass
    class Puzzle:
        instructions: list["Solution.Instruction"]
        regs: dict[str, int]

        def solve(self) -> int:
            i = 0
            while i < len(self.instructions):
                ins = self.instructions[i]
                i += 1
                op, lhs, rhs = ins.op, ins.lhs, ins.rhs
                match op:
                    case Solution.Operation.CPY:
                        if not isinstance(rhs, str):
                            continue
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
                    case Solution.Operation.TGL:
                        lhs = lhs if isinstance(lhs, int) else self.regs[lhs]
                        tgl_i = lhs + i - 1
                        if tgl_i < 0 or tgl_i >= len(self.instructions):
                            continue
                        tgl_op = Solution.Operation.INC
                        match self.instructions[tgl_i].op:
                            case Solution.Operation.CPY:
                                tgl_op = Solution.Operation.JNZ
                            case Solution.Operation.INC:
                                tgl_op = Solution.Operation.DEC
                            case Solution.Operation.JNZ:
                                tgl_op = Solution.Operation.CPY
                            case _:
                                tgl_op = Solution.Operation.INC
                        self.instructions[tgl_i].op = tgl_op
            return self.regs["a"]

    # @answer(1234)
    def part_1(self) -> int:
        instructions: List[Solution.Instruction] = Solution.parse_input(self.input)
        regs: Dict[str, int] = {
            'a': 7,
            'b': 0,
            'c': 0,
            'd': 0,
        }
        return Solution.Puzzle(instructions, regs).solve()

    # @answer(1234)
    def part_2(self) -> int:
        instructions = Solution.parse_input(self.input)
        a_vals = []
        for i in range(7, 11):
            regs: Dict[str, int] = {
                'a': i,
                'b': 0,
                'c': 0,
                'd': 0,
            }
            a = Solution.Puzzle(copy.deepcopy(instructions), regs).solve()
            a_vals.append((i, a))
            print("  {}: {}".format(i, a))

        # Pattern:
        # x_7  =   14445
        # x_8  =   49725
        # x_9  =  372285
        # x_10 = 3638205

        # (372285 - 49725) / 8 - (49725 - 14445) = 5040
        # (3638205 - 372285) / 9 - (372285 - 49725) - (49725 - 14445) = 5040

        # (x_11 - 3638205) / 10 - (3638205 - 372285) - (372285 - 49725) - (49725 - 14445) = 5040
        # x_11 = 39926205

        # (x_12 - 39926205) / 11 - (39926205 - 3638205) - (3638205 - 372285) - (372285 - 49725) - (49725 - 14445) = 5040
        # x_12 = 479011005
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
