# https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        cc = code + code
        for i in range(len(code)):
            if k > 0:
                code[i] = sum(cc[i+1:i+k+1])
            elif k < 0:
                code[i] = sum(cc[i + len(code) + k:i + len(code)])
            else:
                code[i] = 0
        return code