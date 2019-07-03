'''
Let d(n) be defined as the sum of proper
divisors of n (numbers less than n which
divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b,
then a and b are an amicable pair and each
of a and b are called amicable numbers.

For example, the proper divisors of 220
are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and
110; therefore d(220) = 284. The proper
divisors of 284 are 1, 2, 4, 71 and 142;
so d(284) = 220.

Evaluate the sum of all the amicable
numbers under 10000.
'''

amicable = []
sumA = 0
testNum = 1

def sumDivisors(num):
    factors = []
    i = 1
    while i <= num/2:
        if num%i == 0:
            b = int(num / i)
            if i not in factors and b < num:
                factors.append(i)
                factors.append(b)
            elif i not in factors:
                factors.append(i)
        i+=1

    return sum(factors)

for testNum in range(1, 10001):
    first = sumDivisors(testNum)
    second = sumDivisors(first)

    if testNum == second and testNum != first and testNum not in amicable:
        amicable.append(testNum)
        amicable.append(first)

print(sum(amicable))










    
