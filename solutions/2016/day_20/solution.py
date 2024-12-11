# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/20

from ...base import StrSplitSolution, answer
from typing import Optional
from dataclasses import dataclass

class Solution(StrSplitSolution):
    _year = 2016
    _day = 20

    @dataclass
    class BlockRange:
        start: int
        end: int

        def is_blocked(self, ip: int) -> bool:
            return self.start <= ip and ip <= self.end

        def try_merge(self, start: int, end: int) -> bool:
            if (start < self.start and end < self.start) or (self.end < start and self.end < end):
                return False
            self.start = min(self.start, start)
            self.end = max(self.end, end)
            return True

    @dataclass
    class Blocklist:
        blocked: list["Solution.BlockRange"]

        def is_blocked(self, ip: int) -> bool:
            for br in self.blocked:
                if ip < br.start:
                    break
                if br.is_blocked(ip):
                    return True
            return False

        def sort(self):
            self.blocked = sorted(self.blocked, key=lambda x: x.start)

        def add_rule(self, start: int, end: int):
            for br in self.blocked:
                if br.try_merge(start, end):
                    return
            self.blocked.append(Solution.BlockRange(start, end))

        def merge(self):
            i = 0
            while i < len(self.blocked):
                j = i + 1
                while j < len(self.blocked):
                    if self.blocked[i].try_merge(self.blocked[j].start, self.blocked[j].end):
                        self.blocked.pop(j)
                        i = -1
                        break
                    j += 1
                i += 1

    @staticmethod
    def parse_input(input: list[str]) -> "Solution.Blocklist":
        blacklist = Solution.Blocklist([])
        for l in input:
            s, e = l.split('-')
            blacklist.add_rule(int(s), int(e))
        return blacklist

    # @answer(1234)
    def part_1(self) -> int:
        blacklist = Solution.parse_input(self.input)
        blacklist.merge()
        blacklist.sort()
        ip = 0
        while blacklist.is_blocked(ip):
            ip += 1
        return ip

    # @answer(1234)
    def part_2(self) -> int:
        blacklist = Solution.parse_input(self.input)
        blacklist.merge()
        ips = 2 ** 32 - 1
        for br in blacklist.blocked:
            ips -= (br.end - br.start + 1)
        return ips + 1

# 112 too low

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
