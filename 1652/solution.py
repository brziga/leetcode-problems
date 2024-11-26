# https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        if k > 0:
            rnge = range(1, k + 1)
        elif k < 0:
            rnge = range(k, 0)
        else:
            return result
        for i in range(n):
            result[i] = sum(code[(i + j) % n] for j in rnge)
        return result