# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/

class Solution:

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        lis, lds = [1] * n, [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j]+1)
        
        for i in range(n - 1, -1, -1):
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], lds[j]+1)
        
        peaks = []
        for i in range(n):
            if lis[i] > 1 and lds[i] > 1:
                peaks.append(lis[i] + lds[i] - 1)
        
        return n - max(peaks)