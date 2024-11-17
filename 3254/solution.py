# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        hm = {}
        i, j = 0, k
        ans = []
        while j <= len(nums):
            curr = tuple(nums[i:j])
            if curr not in hm.keys():
                stat = all(curr[i + 1] - curr[i] == 1 for i in range(len(curr) - 1))
                hm[curr] = max(curr) if stat else -1
            ans.append(hm[curr])
            i += 1
            j += 1
        return ans