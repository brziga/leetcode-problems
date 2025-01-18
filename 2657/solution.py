# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        present_a, present_b = set(), set()
        pref_common = [0] * (n := len(A))
        for i in range(n):
            present_a.add(A[i])
            present_b.add(B[i])
            pref_common[i] = len(present_a & present_b)
        return pref_common