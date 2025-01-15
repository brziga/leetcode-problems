# https://leetcode.com/problems/maximum-average-pass-ratio/

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for c in classes:
            passing, total = c
            old_ratio = passing / total
            new_ratio = (passing + 1) / (total + 1)
            heap.append((-(new_ratio - old_ratio), passing, total))
        heapq.heapify(heap)

        for es in range(extraStudents):
            _, passing, total = heapq.heappop(heap)
            old_ratio = (passing + 1) / (total + 1)
            new_ratio = (passing + 2) / (total + 2)
            heapq.heappush(heap, (-(new_ratio - old_ratio), passing + 1, total + 1))
        
        return sum(e[1]/e[2] for e in heap) / len(heap)