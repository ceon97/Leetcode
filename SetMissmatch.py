

#You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

#You are given an integer array nums representing the data status of this set after the error.

#Find the number that occurs twice and the number that is missing and return them in the form of an array.



class Solution(object):
    def findErrorNums(self, nums):
        dict1={}
        dict2={}
        
        for i in nums:
            dict1[i]=dict1.get(i,0)+1
        
        for i in dict1:
            if dict1[i]==2:
                double=i
        k=set(nums)
        
        for j in k:
            dict2[j]=dict2.get(j,0)+1
        
        for j in range(1,len(nums)+1):
            dict2[j]=dict2.get(j,0)+1
        
        for j in dict2:
            if dict2[j]==1:
                missing=j
        return [double,missing]
