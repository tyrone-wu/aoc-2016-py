# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/22

from ...base import StrSplitSolution, answer
from typing import Dict, Tuple
from dataclasses import dataclass

class Solution(StrSplitSolution):
    _year = 2016
    _day = 22

    @dataclass
    class Node:
        x: int
        y: int
        size: int
        used: int
        avail: int
        use_p: int

    @staticmethod
    def parse_input(input: list[str]) -> dict[(int, int), "Solution.Node"]:
        grid = dict()
        for l in input[2:]:
            l = l.split()
            x_i = l[0].find('x')
            dash_i = l[0].rfind('-')
            x = int(l[0][x_i+1:dash_i])
            y = int(l[0][dash_i+2:])
            size = int(l[1][:-1])
            used = int(l[2][:-1])
            avail = int(l[3][:-1])
            use_p = int(l[4][:-1])
            grid[(x, y)] = Solution.Node(x, y, size, used, avail, use_p)
        return grid

    @staticmethod
    def viable_moves(grid: dict[(int, int), "Solution.Node"]) -> dict[(int, int), (int, int)]:
        grid_vals = grid.values()
        viable = dict()
        for (i, a) in enumerate(grid_vals):
            if a.used == 0:
                continue
            for (j, b) in enumerate(grid_vals):
                if i == j:
                    continue
                if b.avail >= a.used:
                    viable[(a.x, a.y)] = (b.x, b.y)
        return viable

    # @answer(1234)
    def part_1(self) -> int:
        grid: Dict[Tuple[int, int], Solution.Node] = Solution.parse_input(self.input)
        return len(Solution.viable_moves(grid))

    # @answer(1234)
    def part_2(self) -> int:
        grid = Solution.parse_input(self.input)
        x_high = sorted(grid.keys(), key=lambda x: x[0], reverse=True)[0][0]
        y_high = sorted(grid.keys(), key=lambda x: x[1], reverse=True)[0][1]
        for y in range(y_high + 1):
            row = []
            for x in range(x_high + 1):
                n = grid[(x, y)]
                if n.used == 0:
                    row.append("_")
                elif n.used > 100:
                    row.append("#")
                else:
                    row.append(".")
            print("".join(row))
        return len(".................") + 10 + len("....................................") + 12 + 1 + 5 * len("....................................")

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
