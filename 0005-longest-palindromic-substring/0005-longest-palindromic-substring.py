class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        i=0
        j=0
        ans=""
        while i<len(s):
            if j<len(s):
                a=s[i:j+1]
                if a==a[::-1]:
                    if len(a)>len(ans):
                        ans=a
                j+=1
            else:
                i+=1
                j=i
        return ans