# https://leetcode.com/problems/longest-happy-string/description/

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for e in ([-a, "a"], [-b, "b"], [-c, "c"]):
            if e[0] != 0:
                heap.append(e)
        # heap = [[-a, "a"], [-b, "b"], [-c, "c"]]
        heapq.heapify(heap)
        result = ""

        curr = heapq.heappop(heap)
        if curr[0] == 0:
            return result
        result += curr[1]
        heapq.heappush(heap, [curr[0] + 1, curr[1]])

        while heap:
            curr = heapq.heappop(heap)
            if result[-2::] == curr[1] + curr[1]:
                if not heap:
                    return result
                scnd = heapq.heappop(heap)
                result += scnd[1]
                scnd[0] += 1
                if scnd[0] != 0:
                    heapq.heappush(heap, scnd)
                heapq.heappush(heap, curr)
            else:
                result += curr[1]
                curr[0] += 1
                if curr[0] != 0:
                    heapq.heappush(heap, curr)
        return result
