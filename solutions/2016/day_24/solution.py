# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/24

from ...base import StrSplitSolution, answer
from typing import Dict, List
from collections import deque

class Solution(StrSplitSolution):
    _year = 2016
    _day = 24

    @staticmethod
    def points_of_interest(map: list[str]) -> dict[int, tuple[int, int]]:
        pois = dict()
        for (y, row) in enumerate(map):
            for (x, c) in enumerate(row):
                if c != '#' and c != '.':
                    pois[int(c)] = (x, y)
        return pois

    @staticmethod
    def shortest_dist(map: list[list[str]], start: tuple[int, int]) -> dict[int, int]:
        x, y = start
        dists = dict()
        bfs = deque([(x, y, 0)])
        visited = {(x, y)}
        while bfs:
            x, y, steps = bfs.popleft()
            space = map[y][x]
            if space != '#' and space != '.' and int(space) not in dists:
                space = int(space)
                dists[space] = steps
            if map[y - 1][x] != '#' and (x, y - 1) not in visited:
                visited.add((x, y - 1))
                bfs.append((x, y - 1, steps + 1))
            if map[y][x - 1] != '#' and (x - 1, y) not in visited:
                visited.add((x - 1, y))
                bfs.append((x - 1, y, steps + 1))
            if map[y + 1][x] != '#' and (x, y + 1) not in visited:
                visited.add((x, y + 1))
                bfs.append((x, y + 1, steps + 1))
            if map[y][x + 1] != '#' and (x + 1, y) not in visited:
                visited.add((x + 1, y))
                bfs.append((x + 1, y, steps + 1))
        return dists

    @staticmethod
    def dfs(graph: dict[int, dict[int, int]], visited: int, s: int, p2: bool) -> int:
        min_steps = None
        for (e, dist) in graph[s].items():
            if visited & (1 << e) != 0:
                continue
            steps = dist + Solution.dfs(graph, visited | (1 << e), e, p2)
            if min_steps:
                min_steps = min(min_steps, steps)
            else:
                min_steps = steps
        extra = graph[s][0] if min_steps == None and p2 else 0
        return extra if min_steps == None else min_steps

    @staticmethod
    def tsp(graph: dict[int, dict[int, int]]):
        pass

    # @answer(1234)
    def part_1(self) -> int:
        map: List[List[str]] = [list(row) for row in self.input]
        points = Solution.points_of_interest(map)
        graph: Dict[int, Dict[int, int]] = dict()
        for (p, (x, y)) in points.items():
            graph[p] = Solution.shortest_dist(map, (x, y))
        return Solution.dfs(graph, (1 << 0), 0, False)

    # @answer(1234)
    def part_2(self) -> int:
        map: List[List[str]] = [list(row) for row in self.input]
        points = Solution.points_of_interest(map)
        graph: Dict[int, Dict[int, int]] = dict()
        for (p, (x, y)) in points.items():
            graph[p] = Solution.shortest_dist(map, (x, y))
        return Solution.dfs(graph, (1 << 0), 0, True)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
