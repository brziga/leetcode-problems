# https://leetcode.com/problems/move-pieces-to-obtain-a-string/

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # if Counter(start) != Counter(target): return False
        i, j = 0, 0
        while True:
            while i < len(start) and start[i] == "_":
                i += 1
            while j < len(target) and target[j] == "_":
                j += 1
            if (i >= len(start)) ^ (j >= len(target)): return False
            elif (i >= len(start)) and (j >= len(target)): break
            elif start[i] != target[j]: return False
            elif start[i] == "L" and i < j: return False
            elif start[i] == "R" and i > j: return False
            i += 1
            j += 1
        return True