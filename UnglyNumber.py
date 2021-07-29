
#An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

#Given an integer n, return true if n is an ugly number.

class Solution(object):
    def isUgly(self, n):
        if n==1 or n==2 or n==3 or n==5:
            return True
        elif n==0:
            return False
        else:
                k=[2,3,5]
                for i in k:
                    while n%i==0:
                        n=n/i
                if n==1:
                    return True
                else:
                    return False
                        
