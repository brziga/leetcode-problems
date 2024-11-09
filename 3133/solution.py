class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # ans = [x]
        # prefixes = [x]
        # nxt = x + 1
        # for i in range(1, n):
        #     while nxt & prefixes[-1] != x:
        #         nxt += 1
        #     ans.append(nxt)
        #     prefixes.append(prefixes[-1] & nxt)
        #     nxt += 1
        # # print(ans)
        # return ans[-1]

        xbin = bin(x)[2:]
        xlen, xzeros = len(xbin), xbin.count('0')
        nbin = f"{n-1:0{xlen}b}"

        j = -1
        res = list(xbin)
        for i in range(xlen-1, -1, -1):
            if res[i] != "1":
                res[i] = nbin[j]
                j -= 1
        res = nbin[:len(nbin) - xzeros] + "".join(res)
        # print(res)
        return int(res, 2)