# https://leetcode.com/problems/longest-square-streak-in-an-array

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        innums = set(nums)
        sequences = []
        for n in innums:
            sequences.append([n])
            while True:
                nxt = sequences[-1][-1] ** 2
                if nxt in innums:
                    sequences[-1].append(nxt)
                else:
                    break
        sequences.sort(key = lambda x: len(x), reverse = True)
        return len(sequences[0]) if len(sequences[0]) >= 2 else -1