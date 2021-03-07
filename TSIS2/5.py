class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        umn = 1
        summa = 0
        n = str(n)
        for i in n:
            summa += int(i)
            umn *= int(i)
        return(umn-summa)
