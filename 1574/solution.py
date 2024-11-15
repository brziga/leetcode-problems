# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return 0

        # find longest non-deacreasing subarray from the start
        longleft = 1 # longest from left, non-inclusive
        while arr[longleft] >= arr[longleft - 1]:
            longleft += 1
            if longleft == n: return 0
        
        # same for the end (from the right)
        longright = 1
        while arr[-longright - 1] <= arr[-longright]:
            longright += 1
        
        # find how many elems from the right need to be removed to make concat sorted for each elem in left
        left = [longright] * longleft
        j = 0
        for i in range(longleft):
            while j < longright and arr[-longright:][j] < arr[i]:
                j += 1
            if j >= longright: break
            left[i] = j
        left.append(0)# if we were to remove all elems from left, none would have to be removed from right
        
        # same for the left
        right = [longleft] * longright
        j = 0
        for i in range(-1, -longright - 1, -1):
            while j < longleft and arr[:longleft][-j - 1] > arr[-longright:][i]:
                j += 1
            if j >= longleft: break
            right[i] = j
        right.append(0) # if we were to remove all elems from right, none would have to be removed from left

        print(left); print(right)
        # now find lowest combination
        lowest = n
        for l in left:
            c = l + right[l]
            lowest = min(c, lowest)
        
        return lowest + n - longleft - longright