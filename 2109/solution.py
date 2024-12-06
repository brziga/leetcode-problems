# https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        for i in range(len(spaces)):
            spaces[i] += i
        i, j = 0, 0
        res = []
        while i < len(s) + len(spaces):
            if j < len(spaces) and i == spaces[j]:
                res.append(" ")
                j += 1
            else:
                res.append(s[i - j])
            i += 1
        return "".join(res)