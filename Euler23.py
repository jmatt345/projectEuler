'''
A perfect number is a number for which the
sum of its proper divisors is exactly equal
to the number. For example, the sum of the
proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28
is a perfect number.

A number n is called deficient if the sum of
its proper divisors is less than n and it is
called abundant if this sum exceeds n.

As 12 is the smallest abundant number,
1 + 2 + 3 + 4 + 6 = 16, the smallest number
that can be written as the sum of two abundant
numbers is 24. By mathematical analysis, it
can be shown that all integers greater than
28123 can be written as the sum of two abundant
numbers. However, this upper limit cannot be
reduced any further by analysis even though it
is known that the greatest number that cannot
be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which
cannot be written as the sum of two abundant
numbers.
'''

abundant = []
deficient = []
perfect = []
topEnd = 28123
solution = list(range(1, topEnd + 1))
testNum = 1

def sumDivisors(num):
    factors = []
    i = 1
    while i <= num/2:
        if num%i == 0:
            b = int(num / i)
            if i not in factors and i != b and b < num:
                factors.append(i)
                factors.append(b)
            elif i not in factors:
                factors.append(i)
        i+=1

    return sum(factors)

for testNum in range(1, topEnd):
    if sumDivisors(testNum) > testNum:
        abundant.append(testNum)

for j in abundant:
    for k in abundant:
        if j + k in solution:
            solution.remove(j+k)
    
print(sum(solution))
