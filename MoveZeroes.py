

#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.


class Solution(object):
    def moveZeroes(self, nums):
        
        
        count_zero=0
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
            if nums[i]==0:
                count_zero+=1
        for i in range(len(nums)-count_zero,len(nums)):
            nums[i]=0
        return nums
