# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/25

from ...base import StrSplitSolution, answer
from typing import Dict, List
from dataclasses import dataclass
from enum import Enum, auto
import copy

class Solution(StrSplitSolution):
    _year = 2016
    _day = 25

    class Operation(Enum):
        CPY = auto()
        INC = auto()
        DEC = auto()
        JNZ = auto()
        TGL = auto()
        OUT = auto()

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
            "out": Solution.Operation.OUT,
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

        def solve(self) -> list[int]:
            out = []
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
                    case Solution.Operation.OUT:
                        lhs = lhs if isinstance(lhs, int) else self.regs[lhs]
                        out.append(lhs)
                        if len(out) == 50:
                            return out
            return out

    # @answer(1234)
    def part_1(self) -> int:
        instructions = Solution.parse_input(self.input)
        i = 0
        while True:
            regs: Dict[str, int] = {
                'a': i,
                'b': 0,
                'c': 0,
                'd': 0,
            }
            out = Solution.Puzzle(copy.deepcopy(instructions), regs).solve()
            alternating = True
            for (j, b) in enumerate(out[:-1]):
                if b == out[j + 1]:
                    alternating = False
                    break
            if alternating:
                # print("=== winner: ", i)
                return i
            # print("{:02d}: {}".format(i, "".join([str(b) for b in out])))
            i += 1
        return -1

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
