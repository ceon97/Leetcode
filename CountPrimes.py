
#Count the number of prime numbers less than a non-negative number, n.


class Solution(object):
    def countPrimes(self, n):
        if n<=2:
            return 0
        else:
            prime=[True for i in range(n)]
            prime[0]=False
            prime[1]=False
            p=2
            k=0
            while p*p<=n:
                if prime[p]:
                    for i in range(p*p,n,p):
                        prime[i]=False
                p+=1
            for i in range(n):
                if prime[i]:
                    k+=1
            return(k)
