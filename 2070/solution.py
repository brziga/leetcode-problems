# https://leetcode.com/problems/most-beautiful-item-for-each-query/

class Solution:
    def binSearch(self, array, x):
        left, right = 0, len(array)
        res = array[0]
        while left < right:
            mid = (left + right) // 2
            if array[mid] == x: return x
            elif array[mid] < x:
                res = max(res, array[mid])
                left = mid + 1
            else:
                right = mid
        return res

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        sp = sorted(items, key = lambda x: x[0]) # sorted by price ASC
        mb = {} # most beautiful - {max_price: most_beaut}
        mb[sp[0][0]] = sp[0][1]
        prices = [x[0] for x in sp]
        for i in range(1, len(sp)):
            item = sp[i]
            mb[item[0]] = max(item[1], mb[sp[i-1][0]])
        
        ans = []
        for q in queries:
            if q < prices[0]: ans.append(0)
            elif q not in mb:
                key = self.binSearch(prices, q)
                ans.append(mb[key])
            else:
                ans.append(mb[q])
        return ans