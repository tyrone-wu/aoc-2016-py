# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/16

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2016
    _day = 16

    @staticmethod
    def gen_data(a: list[bool]) -> list[bool]:
        b = a.copy()
        b.reverse()
        b = [not b for b in b]
        return a + [False] + b

    @staticmethod
    def calc_checksum(data: list[bool]) -> list[bool]:
        prev = data
        checksum = []
        while len(checksum) % 2 == 0:
            checksum = []
            i = 0
            while i + 2 <= len(prev):
                pair = prev[i:i + 2]
                checksum.append(pair[0] == pair[1])
                i += 2
            prev = checksum
        return checksum

    @staticmethod
    def solve_puzzle(data: list[bool], len_max: int) -> str:
        while len(data) < len_max:
            data = Solution.gen_data(data)
        checksum = Solution.calc_checksum(data[:len_max])
        return ''.join(['1' if b else '0' for b in checksum])

    # @answer(1234)
    def part_1(self) -> str:
        data = [True if b == '1' else False for b in list(self.input[0])]
        return Solution.solve_puzzle(data, 272)

    # @answer(1234)
    def part_2(self) -> str:
        data = [True if b == '1' else False for b in list(self.input[0])]
        return Solution.solve_puzzle(data, 35651584)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
