# https://leetcode.com/problems/minimize-xor/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n = 32
        num_set_bits = Counter(str(bin(num2)))["1"]
        num1_bin = format(num1, "0"+str(n)+"b")
        num1_set_bits = Counter(num1_bin)["1"]
        zeros_to_set = num_set_bits - num1_set_bits

        x = ["0"] * n
        i = 0
        while i < n and num_set_bits > 0:
            if num1_bin[i] == "1":
                num_set_bits -= 1
                x[i] = "1"
            i += 1
        i = n - 1
        while i >= 0 and num_set_bits > 0:
            if num1_bin[i] == "0" and zeros_to_set > 0:
                zeros_to_set -= 1
                num_set_bits -= 1
                x[i] = "1"
            i -= 1
        
        return int("".join(x), 2)