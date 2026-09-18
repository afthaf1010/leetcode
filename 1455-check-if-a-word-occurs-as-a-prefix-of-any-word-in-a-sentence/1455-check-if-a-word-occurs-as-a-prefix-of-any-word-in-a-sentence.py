class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        a=sentence.split()
        c=1
        for i in a:
            if i.startswith(searchWord):
                return c
            else:
                c+=1
        else:
            return -1