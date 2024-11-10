# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

class Solution:
    def minimumSubarrayLength(self, nums, k: int) -> int:
        start, end = 0, 1
        winor = -1
        numbits = [0] * 32
        shortest = len(nums) + 1

        while end <= len(nums):
            addbits = [int(b) for b in f"{nums[end-1]:032b}"]
            for i in range(32):
                numbits[i] += addbits[i]
            winor = int("".join(["0" if b == 0 else "1" for b in numbits]), 2)

            if winor >= k:
                while start < end - 1:
                    removed = nums[start]
                    rembits = [int(b) for b in f"{removed:032b}"]
                    nbtemp = copy.copy(numbits)
                    for i in range(32):
                        nbtemp[i] -= rembits[i]
                    winor = int("".join(["0" if b == 0 else "1" for b in nbtemp]), 2)
                    if winor >= k:
                        start += 1
                        numbits = nbtemp
                    else:
                        break
                shortest = end - start if end - start < shortest else shortest
                if shortest == 1: return 1 # no need to continue
            end += 1
            
        
        return shortest if shortest <= len(nums) else -1
