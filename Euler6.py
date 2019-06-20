'''
Find the difference between the sum of the
squares and the square of the sum for the
first one hundred natural numbers.
'''

a = 0
sumsq = []

for b in range(1, 101):
    sumsq.append(b * b)

for i in range(1, 101):
    a = a + i
sqosum = a * a

print(sqosum - sum(sumsq))
