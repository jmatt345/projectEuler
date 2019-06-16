# What is the largest prime factor of the number 600851475143 ?

i = 1
a = 600851475143
factors = []

def isPrime(b):
    prime = True
    i = 3
    print("Prime test:", b)
    while i <= int(b/2):
        if b%i == 0:
            print("Not a prime.")
            prime = False
            break
        else:
            i+=2
    if prime == True:
        return b
    else:
        return 0         

while i <= a/2 :
    if a%i == 0:
        b = int(a / i)
        print(i, b)
        if i not in factors:
            factors.append(i)
            factors.append(b)
        else:
            break
    i+=2

factors.sort(reverse=True)
for i in factors:
    primeReturn = isPrime(i)
    if primeReturn > 0:
        break

print("The largest prime factor of", a,"is",primeReturn)
