# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/11

from ...base import StrSplitSolution, answer
from typing import Dict, List, Set, Optional
from dataclasses import dataclass
from copy import deepcopy
from collections import deque

class Solution(StrSplitSolution):
    _year = 2016
    _day = 11

    @dataclass(frozen=True)
    class Floor:
        gens: set[str]
        chips: set[str]

        def __hash__(self):
            return hash((frozenset(self.gens), frozenset(self.chips)))

        def __eq__(self, value):
            return hash(self) == hash(value)

        def union(self, f: "Solution.Floor") -> "Solution.Floor":
            return Solution.Floor(self.gens | f.gens, self.chips | f.chips)

        def difference(self, f: "Solution.Floor") -> "Solution.Floor":
            gens = self.gens.difference(f.gens)
            chips = self.chips.difference(f.chips)
            return Solution.Floor(gens, chips)

        def is_valid(self) -> bool:
            if not self.gens:
                return True
            for c in self.chips:
                if c not in self.gens:
                    return False
            return True

        def is_elev_valid(self, try_flr: "Solution.Floor") -> bool:
            if not self.gens:
                return True
            for c in try_flr.chips:
                if c not in self.gens:
                    return False
            return True

        @staticmethod
        def combos(elements: set[str]) -> list[set[str]]:
            combos: List[Set[str]] = [{}] + [{e} for e in elements]
            elem_l = list(elements)
            for (i, e_i) in enumerate(elem_l):
                for e_j in elem_l[i+1:]:
                    combos.append({e_i, e_j})
            return combos

        def floor_combos(self) -> list["Solution.Floor"]:
            gen_combos = Solution.Floor.combos(self.gens)
            chip_combos = Solution.Floor.combos(self.chips)
            flr_combos = []
            for g in gen_combos:
                for c in chip_combos:
                    if (not g and not c) or (len(g) + len(c) > 2):
                        continue
                    flr_combos.append(Solution.Floor(set(g), set(c)))
            return flr_combos

    @dataclass
    class Area:
        floors: list["Solution.Floor"]
        elev: int

        def __hash__(self):
            flrs = []
            for f in self.floors:
                flrs.append(len(f.gens))
                flrs.append(len(f.chips))
            return hash((tuple(flrs), self.elev))

        def __eq__(self, value):
            return hash(self) == hash(value)

        def is_finished(self) -> bool:
            for f in self.floors[:-1]:
                if f.gens or f.chips:
                    return False
            return True

    @dataclass
    class State:
        area: "Solution.Area"
        steps: int

    @staticmethod
    def parse_floor(line: str) -> Floor:
        line = line.split()
        gen_i = [i for (i, s) in enumerate(line) if s.startswith("gen")]
        chip_i = [i for (i, s) in enumerate(line) if s.endswith("-compatible")]
        gens = set([line[i - 1] for i in gen_i])
        chips = set([line[i][:line[i].find('-')] for i in chip_i])
        return Solution.Floor(gens, chips)

    @staticmethod
    def next_area(floors: list["Solution.Floor"], elev_f: "Solution.Floor", elev: int, step: int) -> Optional["Solution.Area"]:
        rm_flr = floors[elev].difference(elev_f)
        upd_flr = floors[elev + step].union(elev_f)
        if not rm_flr.is_valid() or not upd_flr.is_valid():
            return None
        new_flrs = deepcopy(floors)
        new_flrs[elev] = rm_flr
        new_flrs[elev + step] = upd_flr
        return Solution.Area(new_flrs, elev + step)

    # @answer(1234)
    def part_1(self) -> int:
        start: List[Solution.Floor] = [Solution.parse_floor(l) for l in self.input]
        combos: Dict[Solution.Floor, Set[Solution.Floor]] = dict()
        bfs = deque([Solution.State(Solution.Area(start, 0), 0)])
        seen: Set[Solution.Area] = {Solution.Area(start, 0)}
        while bfs:
            state: Solution.State = bfs.popleft()
            area, steps = state.area, state.steps
            if area.is_finished():
                return steps
            floors, elev = area.floors, area.elev
            if floors[elev] not in combos:
                combos[floors[elev]] = floors[elev].floor_combos()
            flr_combos = combos[floors[elev]]
            if elev + 1 < 4:
                for f in flr_combos:
                    new_area = Solution.next_area(floors, f, elev, 1)
                    if not new_area or new_area in seen:
                        continue
                    seen.add(new_area)
                    bfs.append(Solution.State(new_area, steps + 1))
            if elev > 0:
                for f in flr_combos:
                    new_area = Solution.next_area(floors, f, elev, -1)
                    if not new_area or new_area in seen:
                        continue
                    seen.add(new_area)
                    bfs.append(Solution.State(new_area, steps + 1))
        return None

    # @answer(1234)
    def part_2(self) -> int:
        start: List[Solution.Floor] = [Solution.parse_floor(l) for l in self.input]
        start[0].gens.update(["elerium", "dilithium"])
        start[0].chips.update(["elerium", "dilithium"])
        combos: Dict[Solution.Floor, Set[Solution.Floor]] = dict()
        bfs = deque([Solution.State(Solution.Area(start, 0), 0)])
        seen: Set[Solution.Area] = {Solution.Area(start, 0)}
        while bfs:
            state: Solution.State = bfs.popleft()
            area, steps = state.area, state.steps
            if area.is_finished():
                return steps
            floors, elev = area.floors, area.elev
            if floors[elev] not in combos:
                combos[floors[elev]] = floors[elev].floor_combos()
            flr_combos = combos[floors[elev]]
            if elev + 1 < 4:
                for f in flr_combos:
                    new_area = Solution.next_area(floors, f, elev, 1)
                    if not new_area or new_area in seen:
                        continue
                    seen.add(new_area)
                    bfs.append(Solution.State(new_area, steps + 1))
            if elev > 0:
                for f in flr_combos:
                    new_area = Solution.next_area(floors, f, elev, -1)
                    if not new_area or new_area in seen:
                        continue
                    seen.add(new_area)
                    bfs.append(Solution.State(new_area, steps + 1))
        return None

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
