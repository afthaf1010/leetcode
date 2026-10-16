class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        i=0
        j=0
        a=[]
        while i<len(nums):
            if j<len(nums):
                a.append(nums[i:j+1])
                j+=1
            else:
                i+=1
                j=i
        b=[]
        for i in a:
            n=len(set(i))
            b.append(n*n)
        return sum(b)