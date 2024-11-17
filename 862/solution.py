# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        queue = []
        shortest = n + 1

        for i in range(n + 1):

            while queue and prefix[i] <= prefix[queue[-1]]:
                queue.pop(-1)
            
            queue.append(i)

            while queue and prefix[queue[-1]] - prefix[queue[0]] >= k:
                shortest = queue[-1] - queue[0] if queue[-1] - queue[0] < shortest else shortest
                queue.pop(0)
            
        return shortest if shortest <= n else -1