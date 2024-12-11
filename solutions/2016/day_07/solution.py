# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/7

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2016
    _day = 7

    def contains_abba(self, line: list[chr], win_size: int, aba: set) -> bool:
        contains = False
        for i in range(0, len(line) - win_size + 1):
            window = line[i:i+win_size]
            if len(set(window)) != 2:
                continue
            rev = window.copy()
            rev.reverse()
            if window == rev:
                contains = True
                aba.add(tuple(window))
        return contains

    # @answer(1234)
    def part_1(self) -> int:
        tls_count = 0
        for l in self.input:
            not_brackets = []
            in_brackets = []
            s = 0
            e = 0
            l = list(l)
            for (i, c) in enumerate(l):
                if c == '[':
                    e = i
                    if s < e:
                        not_brackets.append(l[s:e])
                    s = i + 1
                if c == ']':
                    e = i
                    if s < e:
                        in_brackets.append(l[s:e])
                    s = i + 1
            not_brackets.append(l[s:])
            abba = False
            for in_brkt in in_brackets:
                if self.contains_abba(in_brkt, 4, set()):
                    abba = True
                    break
            if abba:
                continue
            for not_in_brkt in not_brackets:
                if self.contains_abba(not_in_brkt, 4, set()):
                    abba = True
                    break
            if abba:
                tls_count += 1
        return tls_count

    # @answer(1234)
    def part_2(self) -> int:
        ssl_count = 0
        for l in self.input:
            not_brackets = []
            in_brackets = []
            s = 0
            e = 0
            l = list(l)
            for (i, c) in enumerate(l):
                if c == '[':
                    e = i
                    if s < e:
                        not_brackets.append(l[s:e])
                    s = i + 1
                if c == ']':
                    e = i
                    if s < e:
                        in_brackets.append(l[s:e])
                    s = i + 1
            not_brackets.append(l[s:])
            aba_in_brkt = set()
            for in_brkt in in_brackets:
                self.contains_abba(in_brkt, 3, aba_in_brkt)
            aba_not_brkt = set()
            for not_in_brkt in not_brackets:
                self.contains_abba(not_in_brkt, 3, aba_not_brkt)
            for brk in aba_in_brkt:
                aba = (brk[1], brk[0], brk[1])
                if aba in aba_not_brkt:
                    ssl_count += 1
                    break
        return ssl_count

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
