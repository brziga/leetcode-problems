# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        largest = max(candidates)
        mlen = len(bin(largest)[2:])
        lengths = [0] * mlen
        bin_cans = [format(c, f"0{mlen}b") for c in candidates]
        for i in range(mlen):
            count = 0
            for bc in bin_cans:
                if bc[i] == "1": count += 1
            lengths[i] = count
        return max(lengths)