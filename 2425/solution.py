# https://leetcode.com/problems/bitwise-xor-of-all-pairings/

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = 32
        set_bits = [0] * n
        for num in nums1:
            num_bin = bin(num)
            for i in range(-1, -len(num_bin) + 1, -1):
                set_bits[i] += int(num_bin[i]) * len(nums2)
        for num in nums2:
            num_bin = bin(num)
            for i in range(-1, -len(num_bin) + 1, -1):
                set_bits[i] += int(num_bin[i]) * len(nums1)
        for i in range(n):
            set_bits[i] = str(set_bits[i] % 2)
        return int("".join(set_bits), 2)