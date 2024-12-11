# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/14

from ...base import StrSplitSolution, answer
import hashlib
from typing import Dict, List, Set

class Solution(StrSplitSolution):
    _year = 2016
    _day = 14

    # @answer(1234)
    def part_1(self) -> int:
        keys_i: Set[int] = set()
        triples: Dict[str, List[int]] = dict()
        i = 0
        while len(keys_i) < 64:
            hash = hashlib.md5((self.input[0] + str(i)).encode("utf-8")).hexdigest()
            hash = list(hash)
            for (j, c) in enumerate(hash[:-5]):
                if hash[j:j + 5] == [c] * 5:
                    if c not in triples:
                        continue
                    for tri_i in triples[c]:
                        if i - tri_i <= 1000:
                            keys_i.add(tri_i)
                            if len(keys_i) == 63:
                                return tri_i
            for (j, c) in enumerate(hash[:-3]):
                if hash[j:j + 3] == [c] * 3:
                    if c not in triples:
                        triples[c] = []
                    triples[c].append(i)
                    break
            i += 1
        return i

    # @answer(1234)
    def part_2(self) -> int:
        keys_i: Set[int] = set()
        triples: Dict[str, List[int]] = dict()
        loops = 1001
        i = 0
        while loops > 0:
            hash = self.input[0] + str(i)
            for _ in range(2017):
                hash = hashlib.md5(hash.encode("utf-8")).hexdigest()
            hash = list(hash)
            for (j, c) in enumerate(hash[:-4]):
                if hash[j:j + 5] == [c] * 5:
                    if c not in triples:
                        continue
                    for tri_i in triples[c]:
                        if i - tri_i <= 1000:
                            keys_i.add(tri_i)
            for (j, c) in enumerate(hash[:-2]):
                if hash[j:j + 3] == [c] * 3:
                    if c not in triples:
                        triples[c] = []
                    triples[c].append(i)
                    break
            if len(keys_i) >= 63:
                loops -= 1
            i += 1
        keys_i = sorted(list(keys_i))
        return keys_i[63]

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
