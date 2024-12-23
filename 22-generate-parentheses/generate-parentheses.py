class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(left,right,comb):
            if len(comb)==n*2:
                res.append(comb)
                return

            if left<n:
                backtrack(left+1,right,comb+"(")

            if right<left:
                backtrack(left,right+1,comb+")")

        backtrack(0,0,"")
        return res

        