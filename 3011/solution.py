# https://leetcode.com/problems/find-if-array-can-be-sorted/

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        segments = [] # [seg_min, seg_max]
        curr_seg_b = -1

        # split to segments of consecutive swapable ints
        # we only need to keep the smallest and largest int
        for i in range(len(nums)):
            n = nums[i]
            b = bin(n)[2:]
            ones = b.count("1")
            if ones == curr_seg_b:
                seg_min, seg_max = segments[-1]
                if n < seg_min:
                    segments[-1] = [n, seg_max]
                elif n > seg_max:
                    segments[-1] = [seg_min, n]
            else:
                segments.append([n, n])
                curr_seg_b = ones
        
        prev = segments[0][1]
        for s in segments[1:]:
            if prev > s[0]: return False
            prev = s[1]
        return True