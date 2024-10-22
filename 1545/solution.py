# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/

class Solution:
    def reverse(self, string):
        return string[::-1]
    def invert(self, string):
        inv = {"0": "1", "1": "0"}
        newstr = ""
        for i in range(len(string)):
            newstr += inv[string[i]]
        return newstr
    def findKthBit(self, n: int, k: int) -> str:
        strings = ["0"]
        for i in range(1, n):
            newstr = strings[i-1] + "1" + Solution.reverse(self, Solution.invert(self, strings[i-1]))
            strings.append(newstr)
        # print(strings)
        return strings[-1][k-1]


# s = Solution()
# r = s.findKthBit(18, 243002)

#TODO: find a better, faster solution
#   - without actually building the strings