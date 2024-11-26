# https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse = True)
        self.scores = nums[:k]
        heapq.heapify(self.scores)
        self.kth = nums[k-1] if len(nums) >= k else -10e4

    def add(self, val: int) -> int:
        if val > self.kth:
            heapq.heappush(self.scores, val)
            while len(self.scores) > self.k:
                heapq.heappop(self.scores)
            self.kth = self.scores[0]
        return self.kth