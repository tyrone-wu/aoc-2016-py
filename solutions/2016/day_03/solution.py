# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/3

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2016
    _day = 3

    # @answer(1234)
    def part_1(self) -> int:
        tri = 0
        for l in self.input:
            lens = [int(len) for len in l.split()]
            lens.sort()
            if lens[0] + lens[1] > lens[2]:
                tri += 1
        return tri

    # @answer(1234)
    def part_2(self) -> int:
        original = []
        for l in self.input:
            original.append([int(len) for len in l.split()])
        input = []
        tri_count = 0
        j = 0
        while j < len(original[0]):
            tri = []
            i = 0
            while i < len(original):
                tri.append(original[i][j])
                i += 1
                if len(tri) == 3:
                    input.append(tri.copy())
                    tri.clear()
            j += 1

        for l in input:
            l.sort()
            if l[0] + l[1] > l[2]:
                tri_count += 1
        return tri_count

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
