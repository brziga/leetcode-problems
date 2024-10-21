# https://leetcode.com/problems/maximum-swap/description/

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10: return num
        possibilities = [num]
        num = list(str(num))
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                newnum = num.copy()
                newnum[i], newnum[j] = newnum[j], newnum[i]
                possibilities.append(int("".join(newnum)))
        possibilities.sort(reverse=True)
        return possibilities[0]