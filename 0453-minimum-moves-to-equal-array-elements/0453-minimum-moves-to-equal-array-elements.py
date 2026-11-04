class Solution:
    def minMoves(self, nums: list[int]) -> int:
        a=min(nums)
        s=0
        for i in range(len(nums)):
            s+=(nums[i]-a)
        return s