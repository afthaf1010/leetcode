class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            p=0
            s=0
            for j in range(i):
                p+=nums[j]
            for j in range(i+1,len(nums)):
                s+=nums[j]
            a.append(abs(p-s))
        return a