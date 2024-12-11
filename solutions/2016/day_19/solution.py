# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/19

from ...base import StrSplitSolution, answer
from dataclasses import dataclass

class Solution(StrSplitSolution):
    _year = 2016
    _day = 19

    # @dataclass
    # class Elf:
    #     id: int
    #     presents: int

    # @answer(1234)
    def part_1(self) -> int:
        elves = int(self.input[0])
        return 2 * (elves - (1 << (elves.bit_length() - 1))) + 1
        # elves = [Solution.Elf(i, 1) for i in range(1, int(self.input[0]) + 1)]
        # i = 0
        # while len(elves) != 1:
        #     j = (i + 1) % len(elves)
        #     elves[i].presents += elves[j].presents
        #     elves.pop(j)
        #     i = j
        # return elves[0].id

    @staticmethod
    def base3(d: int) -> list[int]:
        b3 = []
        while d:
            d, r = divmod(d, 3)
            b3.append(r)
        b3.reverse()
        return b3

    # @answer(1234)
    def part_2(self) -> int:
        start = 1
        end = 100
        for e_len in range(start, end+1):
            elves = [i for i in range(1, e_len + 1)]
            i = 0
            while len(elves) != 1:
                across = (i + len(elves) // 2) % len(elves)
                elves.pop(across)
                if i > across:
                    i -= 1
                i = (i + 1) % len(elves)
            print("===")
            # print("  {0:02d}: {0:08b}".format(e_len, e_len))
            # print("  {0:02d}: {0:08b}".format(elves[0], elves[0]))
            print("  {0:02d}: {1}".format(e_len, ''.join([str(d) for d in Solution.base3(e_len)])))
            print("  {0:02d}: {1}".format(elves[0], ''.join([str(d) for d in Solution.base3(elves[0])])))
        target = int(self.input[0])
        seq = 2
        while seq * 3 - 2 <= target:
            seq = seq * 3 - 2
        elf = 0
        for i in range(seq, target + 1):
            if elf + 1 < seq:
                elf += 1
            else:
                elf += 2
        print(elf)
        return elf

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
