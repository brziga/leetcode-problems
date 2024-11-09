# https://leetcode.com/problems/maximum-xor-for-each-query/description/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        prefixes = [nums[i] if i == 0 else 0 for i in range(n)]
        for i in range(1,n):
            prefixes[i] = prefixes[i-1] ^ nums[i]
        
        answers = [0] * n
        mask = (1 << maximumBit) - 1
        for i in range(n):
            k = ~prefixes[i] & mask
            answers[i] = k
        return answers[::-1]