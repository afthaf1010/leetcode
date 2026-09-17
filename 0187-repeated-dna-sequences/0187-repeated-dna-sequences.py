class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        s1=set()
        r=set()
        i=0
        j=9
        while j<len(s):
            x=s[i:j+1]
            if x in s1:
                r.add(x)
            else:
                s1.add(x)
            i+=1
            j+=1
        return list(r)