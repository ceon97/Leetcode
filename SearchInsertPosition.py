#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.



class Solution(object):
    def searchInsert(self, nums, target):
        l=0
        h=len(nums)-1
        m=0
        k=0
        if target>nums[h]:
            return h+1
        while l<=h:
            m=(l+h)//2
            if target==nums[m]:
                return m
            if target<nums[m]:
                h=m-1
                if target>nums[h]:
                    k=l
            else:
                l=m+1
                if target<nums[l]:
                    k=l
        return k
