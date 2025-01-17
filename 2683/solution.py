# https://leetcode.com/problems/neighboring-bitwise-xor/

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        der_xor = 0
        for d in derived: der_xor ^= d
        return not der_xor