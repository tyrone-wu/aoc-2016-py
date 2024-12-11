# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2016
    _day = 1

    # @answer(1234)
    def part_1(self) -> int:
        instructions = self.input[0].split(", ")
        dir = 0 # 0 N, 1 E, 2 S, 3 W
        x, y = 0, 0
        for insns in instructions:
            if insns[0] == 'R':
                dir = (dir + 1) % 4
            else:
                dir = abs(dir + 3) % 4
            steps = int(insns[1:])
            match dir:
                case 0:
                    x += steps
                case 1:
                    y += steps
                case 2:
                    x -= steps
                case _:
                    y -= steps
        return abs(x) + abs(y)

    # @answer(1234)
    def part_2(self) -> int:
        instructions = self.input[0].split(", ")
        dir = 0 # 0 N, 1 E, 2 S, 3 W
        x, y = 0, 0
        locs = set((0, 0))
        for insns in instructions:
            if insns[0] == 'R':
                dir = (dir + 1) % 4
            else:
                dir = abs(dir + 3) % 4
            steps = int(insns[1:])
            for _ in range(0, steps):
                match dir:
                    case 0:
                        x += 1
                    case 1:
                        y += 1
                    case 2:
                        x -= 1
                    case _:
                        y -= 1
                coord = (x, y)
                if coord in locs:
                    return abs(x) + abs(y)
                locs.add(coord)
        return 0

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
