import numpy as n
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return int(n.partition(nums,-k)[-k])