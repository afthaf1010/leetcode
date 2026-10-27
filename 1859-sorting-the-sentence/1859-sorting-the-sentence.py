class Solution:
    def sortSentence(self, s: str) -> str:
        a=[]
        k=s.split()
        for i in range(1,len(s)+1):
            for j in k:
                if str(i) in j:
                    a.append(j[:-1])
                else:
                    continue
        return " ".join(a)