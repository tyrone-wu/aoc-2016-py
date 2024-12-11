# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/13

from ...base import StrSplitSolution, answer
from typing import NamedTuple, Set, Optional
from collections import deque

class Solution(StrSplitSolution):
    _year = 2016
    _day = 13

    class Coord(NamedTuple):
        x: int
        y: int

        def is_open(self, fav: int) -> bool:
            if self.x < 0 or self.y < 0:
                return False
            res = self.x * (self.x + 3) + 2 * self.x * self.y + self.y * (self.y + 1)
            res += fav
            return bin(res).count('1') % 2 == 0

    class Step(NamedTuple):
        coord: "Solution.Coord"
        steps: int

    # @answer(1234)
    def part_1(self) -> int:
        fav = int(self.input[0])
        target = Solution.Coord(31, 39)
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        bfs = deque([Solution.Step(Solution.Coord(1, 1), 0)])
        seen: Set[Solution.Coord] = set()
        while bfs:
            state = bfs.popleft()
            coord, steps = state
            if coord == target:
                return steps
            for dx, dy in moves:
                move_coord = Solution.Coord(coord.x + dx, coord.y + dy)
                if move_coord not in seen and move_coord.is_open(fav):
                    seen.add(move_coord)
                    bfs.append(Solution.Step(move_coord, steps + 1))
        return None

    # @answer(1234)
    def part_2(self) -> int:
        fav = int(self.input[0])
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        start = Solution.Coord(1, 1)
        bfs = deque([Solution.Step(start, 0)])
        seen: Set[Solution.Coord] = set([start])
        while bfs:
            state = bfs.popleft()
            coord, steps = state
            if steps == 50:
                continue
            for dx, dy in moves:
                move_coord = Solution.Coord(coord.x + dx, coord.y + dy)
                if move_coord not in seen and move_coord.is_open(fav):
                    seen.add(move_coord)
                    bfs.append(Solution.Step(move_coord, steps + 1))
        return len(seen)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
