# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        # find all subarrays
        subas = [[]]
        for num in nums:
            new_subsequences = [curr + [num] for curr in subas]
            subas.extend(new_subsequences)
        subas.remove([])
        
        # calc bitwise ORs for the subarrays
        maxi = Solution.bitwiseORArray(self, subas[0])
        count = 1
        for i in subas[1:]:
            ibor = Solution.bitwiseORArray(self, i)
            if ibor > maxi:
                maxi = ibor
                count = 1
            elif ibor == maxi:
                count +=1
        
        return count

    def bitwiseORArray(self, nums: List[int]) -> int:
        bor = 0
        for i in nums:
            bor = bor | i
        return bor