# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/5

from ...base import StrSplitSolution, answer
import hashlib

class Solution(StrSplitSolution):
    _year = 2016
    _day = 5

    # @answer(1234)
    def part_1(self) -> str:
        password = []
        i = 0
        while len(password) < 8:
            hash = hashlib.md5((self.input[0] + str(i)).encode("utf-8")).hexdigest()
            if hash.startswith("00000"):
                password.append(hash[5])
            i += 1
        return ''.join(password)

    # @answer(1234)
    def part_2(self) -> str:
        password = [' '] * 8
        bit = 0
        i = 0
        while bit != (1 << 8) - 1:
            hash = hashlib.md5((self.input[0] + str(i)).encode("utf-8")).hexdigest()
            if hash.startswith("00000") and hash[5].isdigit():
                pos = int(hash[5])
                if 0 <= pos and pos <= 7 and (bit & (1 << pos)) == 0:
                    password[pos] = hash[6]
                    bit |= 1 << pos
            i += 1
        return ''.join(password)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
