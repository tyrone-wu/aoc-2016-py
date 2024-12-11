# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/9

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2016
    _day = 9

    # @answer(1234)
    def part_1(self) -> int:
        seq = self.input[0]
        decomp = []
        win_s = 0
        is_comp = False
        i = 0
        while i < len(seq):
            c = seq[i]
            if c == '(':
                is_comp = True
                win_s = i + 1
            elif c == ')':
                is_comp = False
                win_size, repeat = [int(n) for n in seq[win_s:i].split('x')]
                for _ in range(0, repeat):
                    decomp.extend(seq[i+1:i+1+win_size])
                i += win_size
            else:
                if not is_comp:
                    decomp.append(c)
            i += 1
        return len(decomp)

    def decompress(self, input: str) -> int:
        op_br = input.find('(')
        cl_br = input.find(')')
        if op_br == -1:
            return len(input)
        decomp = op_br
        win_size, repeat = [int(n) for n in input[op_br+1:cl_br].split('x')]
        decomp += repeat * self.decompress(input[cl_br+1:cl_br+1+win_size]) + self.decompress(input[cl_br+1+win_size:])
        return decomp

    # @answer(1234)
    def part_2(self) -> int:
        return self.decompress(self.input[0])

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
