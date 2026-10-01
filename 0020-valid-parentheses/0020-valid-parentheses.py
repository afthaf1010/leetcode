class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i in "({[":
                l.append(i)
            else:
                if len(l) == 0:
                    return False
                top = l.pop()
                if (i == "}" and top != "{") or (i == ")" and top != "(") or (i == "]" and top != "["):
                    return False
        if len(l) == 0:
            return True
        else:
            return False