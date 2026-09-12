class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        dp = [0] * n
        m = height[0]
        for i in range(n):
            m = max(m, height[i])
            dp[i] = m
        m = height[n - 1]
        ans = 0
        for i in range(n - 1, -1, -1):
            m = max(m, height[i])
            water = min(dp[i], m) - height[i]
            ans += water
        return ans