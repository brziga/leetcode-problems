# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/

class Solution:
    
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        # split to all the subarrays
        n_suba = len(nums) - k + 1 # n - k + 1
        subarrays = []
        for i in range(n_suba):
            subarrays.append(nums[i:i+k])
        # print(subarrays)
        
        results = []
        for sa in subarrays:
            results.append(Solution.xSumCalc(self, sa, x))
        
        return results

    def xSumCalc(self, array: List[int], x: int) -> int:
        # print("array:", array)
        hm = {} # occurences {num: occ}
        for n in array:
            if n in hm.keys():
                hm[n] += 1
            else:
                hm[n] = 1
                
        pairs = list(hm.items())
        pairs.sort(key=lambda x: (x[1], x[0]), reverse=True)
        # print(pairs)
        pairs = pairs[0:x]
        # print(pairs)
        
        result = sum(p[0]*p[1] for p in pairs)
        
        return result