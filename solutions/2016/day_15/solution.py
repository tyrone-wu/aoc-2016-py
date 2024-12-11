# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/15

from ...base import StrSplitSolution, answer
from typing import List, NamedTuple

class Solution(StrSplitSolution):
    _year = 2016
    _day = 15

    class Disc(NamedTuple):
        id: int
        total_pos: int
        current_pos: int

    @staticmethod
    def parse_input(input: list[str]) -> list["Solution.Disc"]:
        discs = []
        for l in input:
            l = l.split()
            id = int(l[1][1:])
            total_pos = int(l[3])
            current_pos = int(l[11][:-1])
            discs.append(Solution.Disc(id, total_pos, current_pos))
        return discs

    @staticmethod
    def solve_puzzle(discs: list["Solution.Disc"]) -> int:
        t = 0
        while True:
            exit = True
            t_tmp = t
            for d in discs:
                t_tmp += 1
                if (d.current_pos + t_tmp) % d.total_pos != 0:
                    exit = False
                    break
            if exit:
                return t
            t += 1
        return -1

    # @answer(1234)
    def part_1(self) -> int:
        discs: List[Solution.Disc] = Solution.parse_input(self.input)
        return Solution.solve_puzzle(discs)

    # @answer(1234)
    def part_2(self) -> int:
        discs: List[Solution.Disc] = Solution.parse_input(self.input)
        discs.append(Solution.Disc(7, 11, 0))
        return Solution.solve_puzzle(discs)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
