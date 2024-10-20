# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

import heapq

class Solution:
  def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
    heapTimes = [[times[i][0], times[i][1], i] for i in range(len(times))]
    heapq.heapify(heapTimes)
    heapFree = list(range(0, len(times))) # free chairs
    heapq.heapify(heapFree)
    heapOccup = [] # [leave time, chair num]
    targetTime = times[targetFriend][0]
    for i in range(targetTime + 1):
      nextTimeSit = heapTimes[0]
      nextTimeLeave = heapOccup[0][0] if len(heapOccup) > 0 else -1
      while i == nextTimeLeave:
        # person leaves
        chair = heapq.heappop(heapOccup)
        heapq.heappush(heapFree, chair[1])
        nextTimeLeave = heapOccup[0][0] if len(heapOccup) > 0 else -1
      if i == targetTime:
        chair = heapq.heappop(heapFree)
        return chair
      if i == nextTimeSit[0]:
        # person arrived
        arrival = heapq.heappop(heapTimes)
        chair = heapq.heappop(heapFree)
        heapq.heappush(heapOccup, (arrival[1], chair))