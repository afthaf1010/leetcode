class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        i=0
        a=[]
        while i<len(nums):
            if nums[i]<pivot:
                a.append(nums[i])
            i+=1
        i=0
        while i<len(nums):
            if nums[i]==pivot:
                a.append(nums[i])
            i+=1
        i=0
        while i<len(nums):
            if nums[i]>pivot:
                a.append(nums[i])
            i+=1
        return a
        