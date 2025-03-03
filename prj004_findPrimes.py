def findPrimes(n):
    count = 0
    for i in range(2, n+1):
        a     = 0
        for j in range(2, int(n+1/2) + 1): a += 1 if i % j == 0 else False
        if a <= 1 : count += 1
    return count

print(findPrimes(50))

