# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/21

from ...base import StrSplitSolution, answer
import itertools

class Solution(StrSplitSolution):
    _year = 2016
    _day = 21

    @staticmethod
    def scramble(instruction: str, password: list[str]):
        insn = instruction.split()
        op = insn[0:2]
        if op == "swap position".split():
            x, y = int(insn[2]), int(insn[5])
            password[x], password[y] = password[y], password[x]
        elif op == "swap letter".split():
            i, j = password.index(insn[2]), password.index(insn[5])
            password[i], password[j] = password[j], password[i]
        elif op == "rotate left".split() or op == "rotate right".split():
            x = int(insn[2])
            if insn[1] == "right":
                x = -x
            rot = password[x:] + password[:x]
            password.clear()
            password.extend(rot)
        elif op == "rotate based".split():
            x = password.index(insn[6])
            if x >= 4:
                x += 1
            x = -(x + 1) % len(password)
            rot = password[x:] + password[:x]
            password.clear()
            password.extend(rot)
        elif op == "reverse positions".split():
            x, y = int(insn[2]), int(insn[4])
            i, j = min(x, y), max(x, y) + 1
            rev = password[:i] + list(reversed(password[i:j])) + password[j:]
            password.clear()
            password.extend(rev)
        elif op == "move position".split():
            x, y = int(insn[2]), int(insn[5])
            password.insert(y, password.pop(x))

    # @answer(1234)
    def part_1(self) -> str:
        password = list("abcdefgh")
        for insn in self.input:
            Solution.scramble(insn, password)
        return "".join(password)

    # @answer(1234)
    def part_2(self) -> str:
        target = list("fbgdceah")
        for perm in itertools.permutations(target):
            password = list(perm)
            for insn in self.input:
                Solution.scramble(insn, password)
            if password == target:
                return "".join(perm)
        return None

# fbgdceah

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
