# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/18

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2016
    _day = 18

    @staticmethod
    def next_row(row: list[bool]) -> list[bool]:
        next = []
        r_len = len(row)
        for i in range(1, r_len - 1):
            traps = 0
            win = row[i-1:i+2]
            if win == [True, True, False]:
                traps += 1
            if win == [False, True, True]:
                traps += 1
            if row[i - 1] and row[i:i+2] == [False, False]:
                traps += 1
            if row[i + 1] and row[i-1:i+1] == [False, False]:
                traps += 1
            if traps == 1:
                next.append(True)
            else:
                next.append(False)
        return [False] + next + [False]

    @staticmethod
    def solve_puzzle(rows: int, input: str) -> int:
        row = [False] + [c == '^' for c in input] + [False]
        safe = len(row) - sum(row) - 2
        for _ in range(rows - 1):
            row = Solution.next_row(row)
            safe += len(row) - sum(row) - 2
        return safe

    # @answer(1234)
    def part_1(self) -> int:
        return Solution.solve_puzzle(40, self.input[0])

    # @answer(1234)
    def part_2(self) -> int:
        return Solution.solve_puzzle(400000, self.input[0])

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
