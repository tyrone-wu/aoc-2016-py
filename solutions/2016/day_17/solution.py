# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/17

from ...base import StrSplitSolution, answer
from typing import Set, List
from dataclasses import dataclass
import hashlib
from collections import deque

class Solution(StrSplitSolution):
    _year = 2016
    _day = 17

    open = {'b', 'c', 'd', 'e', 'f'}

    @dataclass
    class Hash:
        up: str
        down: str
        left: str
        right: str

        def __init__(self, hash: str):
            self.up = hash[0]
            self.down = hash[1]
            self.left = hash[2]
            self.right = hash[3]

        def __hash__(self):
            return hash((self.up, self.down, self.left, self.right))

    # @answer(1234)
    def part_1(self) -> str:
        bfs = deque([(0, 3, self.input[0])])
        while bfs:
            x, y, passcode = bfs.popleft()
            if x == 3 and y == 0:
                return passcode[len(self.input[0]):]
            hash = hashlib.md5(passcode.encode("utf-8")).hexdigest()
            hash = Solution.Hash(hash)
            if y < 3 and hash.up in Solution.open:
                bfs.append((x, y + 1, passcode + 'U'))
            if y > 0 and hash.down in Solution.open:
                bfs.append((x, y - 1, passcode + 'D'))
            if x > 0 and hash.left in Solution.open:
                bfs.append((x - 1, y, passcode + 'L'))
            if x < 3 and hash.right in Solution.open:
                bfs.append((x + 1, y, passcode + 'R'))
        return None

    @staticmethod
    def dfs_maze(x: int, y: int, passcode: str, finished: set[int]):
        if x == 3 and y == 0:
            finished.add(len(passcode))
            return
        hash = hashlib.md5(passcode.encode("utf-8")).hexdigest()
        hash = Solution.Hash(hash)
        if y < 3 and hash.up in Solution.open:
            Solution.dfs_maze(x, y + 1, passcode + 'U', finished)
        if y > 0 and hash.down in Solution.open:
            Solution.dfs_maze(x, y - 1, passcode + 'D', finished)
        if x > 0 and hash.left in Solution.open:
            Solution.dfs_maze(x - 1, y, passcode + 'L', finished)
        if x < 3 and hash.right in Solution.open:
            Solution.dfs_maze(x + 1, y, passcode + 'R', finished)

    # @answer(1234)
    def part_2(self) -> int:
        finished = set()
        Solution.dfs_maze(0, 3, self.input[0], finished)
        return max(finished) - len(self.input[0])

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
