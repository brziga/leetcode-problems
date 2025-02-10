# 

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        numbers = set(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
        for i in range(len(s)):
            if s[i] not in numbers:
                stack.append(s[i])
            else:
                del stack[-1]
        return "".join(stack)