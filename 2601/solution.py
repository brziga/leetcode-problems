# https://leetcode.com/problems/prime-subtraction-operation/

class Solution:
    def largestPrimeUpTo(self, x):
        primes = (
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 
            71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 
            149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 
            227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 
            307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 
            389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 
            467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 
            571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 
            653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 
            751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 
            853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 
            947, 953, 967, 971, 977, 983, 991, 997
        )
        left, right = 0, len(primes) - 1
        while left <= right:
            mid = (left + right) // 2
            if primes[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return primes[right] if right >= 0 else None

    def primeSubOperation(self, nums) -> bool:
        for i in range(len(nums) - 1):
            # if nums[i] < nums[i + 1]:
            #     continue
            prim = self.largestPrimeUpTo(nums[i] - (nums[i-1] if i > 0 else 0))
            nums[i] -= prim if not prim is None else 0
        
        return all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))