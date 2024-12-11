# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2016
    _day = 2

    keypad_p1 = """     
 123 
 456 
 789 
     
"""

    def get_num(self, keypad: list[str], coord: list[int], line: str) -> str:
        for insns in line:
            x, y = 0, 0
            match insns:
                case 'U':
                    x = -1
                case 'D':
                    x = 1
                case 'L':
                    y = -1
                case _:
                    y = 1
            if keypad[coord[0] + x][coord[1] + y] == ' ':
                continue
            coord[0] += x
            coord[1] += y
        return keypad[coord[0]][coord[1]]

    # @answer(1234)
    def part_1(self) -> int:
        keypad = self.keypad_p1.splitlines()
        code = 0
        coord = [2, 2]
        for l in self.input:
            code = code * 10 + int(self.get_num(keypad, coord, l))
        return code

    keypad_p2 = """          
   1   
  234  
 56789 
  ABC  
   D   
       
"""

    # @answer(1234)
    def part_2(self) -> int:
        keypad = self.keypad_p2.splitlines()
        code = ""
        coord = [3, 1]
        for l in self.input:
            code += self.get_num(keypad, coord, l)
        return code

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
