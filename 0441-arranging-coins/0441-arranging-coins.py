class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1:
            return 1
        c=1
        a=n
        for i in range(n):
            a-=c
            if a<0:
                return i
            c+=1
        