# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/8

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2016
    _day = 8

    # @answer(1234)
    def part_1(self) -> int:
        grid = [[False] * 50 for _ in range(0, 6)]
        for l in self.input:
            l = l.split()
            if l[0] == "rect":
                l = l[1].split('x')
                x, y = int(l[0]), int(l[1])
                for i in range(0, y):
                    for j in range(0, x):
                        grid[i][j] = True
            else:
                shift = int(l[4])
                axis = l[2].split('=')
                pos = int(axis[1])
                if l[1] == "row":
                    row = grid[pos]
                    grid[pos] = row[-shift:] + row[:-shift]
                else:
                    col = [col[pos] for col in grid]
                    col = col[-shift:] + col[:-shift]
                    for (i, c) in enumerate(col):
                        grid[i][pos] = c
        count = 0
        for l in grid:
            for x in l:
                if x:
                    count += 1
        return count

    # @answer(1234)
    def part_2(self) -> None:
        grid = [[False] * 50 for _ in range(0, 6)]
        for l in self.input:
            l = l.split()
            if l[0] == "rect":
                l = l[1].split('x')
                x, y = int(l[0]), int(l[1])
                for i in range(0, y):
                    for j in range(0, x):
                        grid[i][j] = True
            else:
                shift = int(l[4])
                axis = l[2].split('=')
                pos = int(axis[1])
                if l[1] == "row":
                    row = grid[pos]
                    grid[pos] = row[-shift:] + row[:-shift]
                else:
                    col = [col[pos] for col in grid]
                    col = col[-shift:] + col[:-shift]
                    for (i, c) in enumerate(col):
                        grid[i][pos] = c
        for l in grid:
            line = []
            for x in l:
                line.append('#' if x else '.')
            print(''.join(line))

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
