# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/4

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2016
    _day = 4

    # @answer(1234)
    def part_1(self) -> int:
        sum = 0
        for l in self.input:
            freq = dict()
            bracket = l.find('[')
            for c in l[:bracket]:
                if c == '-' or c.isdigit():
                    continue
                if c not in freq:
                    freq[c] = 0
                freq[c] += 1

            freq = [(k, v) for k, v in sorted(freq.items(), key=lambda item: (-item[1], item[0]))]
            checksum = [c for c in l[bracket+1:-1]]
            real = True
            for (i, c) in enumerate(checksum):
                if c != freq[i][0]:
                    real = False
                    break
            if real:
                sum += int(l[l.rfind('-')+1:bracket])
        return sum

    # @answer(1234)
    def part_2(self) -> None:
        for l in self.input:
            freq = dict()
            bracket = l.find('[')
            for c in l[:bracket]:
                if c == '-' or c.isdigit():
                    continue
                if c not in freq:
                    freq[c] = 0
                freq[c] += 1

            freq = [(k, v) for k, v in sorted(freq.items(), key=lambda item: (-item[1], item[0]))]
            checksum = [c for c in l[bracket+1:-1]]
            real = True
            for (i, c) in enumerate(checksum):
                if c != freq[i][0]:
                    real = False
                    break
            if real:
                dash = l.rfind('-')
                id = int(l[dash+1:bracket])
                decrypted = ""
                for c in l[:dash]:
                    if c == '-':
                        decrypted += ' '
                        continue
                    rotated = chr((ord(c) - ord('a') + id) % 26 + ord('a'))
                    decrypted += rotated
                print(decrypted + ' ' + str(id))

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
