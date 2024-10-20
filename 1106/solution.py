# https://leetcode.com/problems/parsing-a-boolean-expression/description/?envType=daily-question&envId=2024-10-20

class Solution:
    def splitToTokens(self, expr: str):
        # splits the expression in to subexpressions and leaves their insides untouched
        inParen = 0
        start = 0
        exprs = []
        for i in range(len(expr)):
            c = expr[i]
            if c == "(":
                inParen += 1
            elif c == ")":
                inParen -= 1
            elif c == "," and not inParen > 0:
                exprs.append(expr[start:i])
                start = i+1
        exprs.append(expr[start::])
        return exprs

    def parseBoolExpr(self, expression: str) -> bool:
        match expression[0]:
            case "t": return True
            case "f": return False
            case "!": return not self.parseBoolExpr(expression[2::])
            case "&":
                exprs = Solution.splitToTokens(self, expression[2:-1])
                result = self.parseBoolExpr(exprs[0])
                for e in exprs[1::]:
                    result = result and self.parseBoolExpr(e)
                return result
            case "|":
                exprs = Solution.splitToTokens(self, expression[2:-1])
                result = self.parseBoolExpr(exprs[0])
                # print(result)
                for e in exprs[1::]:
                    result = result or self.parseBoolExpr(e)
                    # print(result)
                return result
            

# test = "|(&(t,f,t),!(t))"
# s = Solution()
# t1 = s.splitToTokens('&(t,f,t),!(t)')
# r = s.parseBoolExpr(test)