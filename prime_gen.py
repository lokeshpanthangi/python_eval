n = int(input())
primes = [2]
for i in range(n):
    c = 0
    if i % 2 != 0:
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                c+=1
        if c < 1:
            primes.append(i)
print(primes)

