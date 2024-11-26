# https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        mp = {i: 0 for i in range(n)} # map

        for i in range(len(edges)):
            edge = edges[i]
            mp[edge[1]] += 1
        
        champs = [key for key, val in mp.items() if val == 0]
        return champs[0] if len(champs) == 1 else -1