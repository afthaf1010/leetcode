class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        m=min(x,y//4)
        if m%2==1:
            return "Alice"
        else:
            return "Bob"