class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(2, int(n**0.5)+1):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
        
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count