# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/6

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2016
    _day = 6

    # @answer(1234)
    def part_1(self) -> str:
        msg = []
        for j in range(0, len(self.input[0])):
            freq = dict()
            for i in range(0, len(self.input)):
                c = self.input[i][j]
                if c not in freq:
                    freq[c] = 0
                freq[c] += 1
            freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
            msg.append(freq[0][0])
        return ''.join(msg)

    # @answer(1234)
    def part_2(self) -> int:
        msg = []
        for j in range(0, len(self.input[0])):
            freq = dict()
            for i in range(0, len(self.input)):
                c = self.input[i][j]
                if c not in freq:
                    freq[c] = 0
                freq[c] += 1
            freq = sorted(freq.items(), key=lambda item: item[1])
            msg.append(freq[0][0])
        return ''.join(msg)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
