class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        stack = []
        for c in s:
            if c == ")":
                stack.pop()
            if len(stack) > 0:
                ans.append(c)
            if c == "(":
                stack.append(c)
        return "".join(ans)