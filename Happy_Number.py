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
