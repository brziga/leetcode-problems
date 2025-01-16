# https://leetcode.com/problems/bitwise-xor-of-all-pairings/

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0: return 0
        n = 32
        set_bits = [0] * n
        if len(nums2) % 2 == 1:
            for num in nums1:
                num_bin = bin(num)
                for i in range(-1, -len(num_bin) + 1, -1):
                    set_bits[i] ^= int(num_bin[i])
        if len(nums1) % 2 == 1:
            for num in nums2:
                num_bin = bin(num)
                for i in range(-1, -len(num_bin) + 1, -1):
                    set_bits[i] ^= int(num_bin[i])
        return int("".join([str(x) for x in set_bits]), 2)