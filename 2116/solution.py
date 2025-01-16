# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if (n := len(s)) % 2 == 1: return False
        locked_left, unlocked = 0, 0
        for i in range(n):
            if locked[i] == "1":
                if s[i] == "(":
                    locked_left += 1
                elif s[i] == ")":
                    if locked_left > 0:
                        locked_left -= 1
                    elif unlocked > 0:
                        unlocked -= 1
                    else:
                        return False
            elif locked[i] == "0":
                unlocked += 1
        balance = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == "0":
                balance += 1
                unlocked -= 0
            elif s[i] == "(":
                balance -= 1
                locked_left -= 1
            elif s[i] == ")":
                balance += 1
            if balance < 0: return False
            if unlocked == 0 and locked_left == 0: break
        
        return locked_left <= 0