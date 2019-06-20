'''
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

prime = 1
primes = [2]
testcase = 3

def isPrime(a):
    prime = True
    i = 3
    
    while i <= int(a/2):
        if a%i == 0:
            prime = False
            break
        else:
            i+=2
    if prime == True:
        return a
    else:
        return 0 

while prime < 10001:
    c = isPrime(testcase)

    if c == 0:
        testcase+=2
    else:
        testcase += 2
        primes.append(c)
        prime += 1

print(max(primes))
    
