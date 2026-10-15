class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        i=0
        a=[]
        b=[]
        c=[]
        while i<len(nums):
            if nums[i]<pivot:
                a.append(nums[i])
            if nums[i]==pivot:
                b.append(nums[i])
            if nums[i]>pivot:
                c.append(nums[i])
            i+=1
        return a+b+c
        