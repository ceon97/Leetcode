"A happy number is a number defined by the following process:"

"Starting with any positive integer, replace the number by the sum of the squares of its digits."
"Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1."
"Those numbers for which this process ends in 1 are happy."
"Return true if n is a happy number, and false if not."



class Solution(object):
    def isHappy(self, n):
        k=set()
        while n!=1:
            c=0
            for i in str(n):
                c=c+(int(i)**2)
            n=c
            if n in k:
                return False
            else:
                k.add(n)
        return True
