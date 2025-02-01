# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(heap)

        for i in range(k):
            num, ind = heapq.heappop(heap)
            heapq.heappush(heap, (num * multiplier, ind))
        
        for num, ind in heap:
            nums[ind] = num
        return nums