# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/10

from ...base import StrSplitSolution, answer
from typing import Dict, List
from dataclasses import dataclass

class Solution(StrSplitSolution):
    _year = 2016
    _day = 10

    @dataclass
    class Give:
        is_bot: bool
        id: int

    @dataclass
    class Instruction:
        low: "Solution.Give"
        high: "Solution.Give"

    def solve_puzzle(self, part_one: bool) -> int:
        bots: Dict[int, List[int]] = dict()
        has_two: List[int] = []
        insns: Dict[int, Solution.Instruction] = dict()
        outputs: Dict[int, int] = dict()
        for l in self.input:
            l = l.split()
            if l[0] == "value":
                v = int(l[1])
                b = int(l[5])
                if b not in bots:
                    bots[b] = []
                bots[b].append(v)
            else:
                b = int(l[1])
                low = Solution.Give(l[5] == "bot", int(l[6]))
                high = Solution.Give(l[10] == "bot", int(l[11]))
                insns[b] = Solution.Instruction(low, high)
        for (b, chips) in bots.items():
            if len(chips) == 2:
                has_two.append(b)
        while has_two:
            b = has_two.pop()
            chips = bots[b]
            min_v, max_v = min(chips), max(chips)
            del bots[b]
            if part_one and min_v == 17 and max_v == 61:
                return b
            insn = insns[b]
            if insn.low.is_bot:
                if insn.low.id not in bots:
                    bots[insn.low.id] = []
                low_chips = bots[insn.low.id]
                low_chips.append(min_v)
                if len(low_chips) == 2:
                    has_two.append(insn.low.id)
            else:
                outputs[insn.low.id] = min_v
            if insn.high.is_bot:
                if insn.high.id not in bots:
                    bots[insn.high.id] = []
                high_chips = bots[insn.high.id]
                high_chips.append(max_v)
                if len(high_chips) == 2:
                    has_two.append(insn.high.id)
            else:
                outputs[insn.high.id] = max_v
        return outputs[0] * outputs[1] * outputs[2]

    # @answer(1234)
    def part_1(self) -> int:
        return self.solve_puzzle(True)

    # @answer(1234)
    def part_2(self) -> int:
        return self.solve_puzzle(False)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
