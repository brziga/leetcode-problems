# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hmap = set()
        for j in jewels:
            hmap.add(j)
        res = 0
        for s in stones:
            if s in hmap: res += 1
        return res