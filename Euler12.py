'''
The sequence of triangle numbers is generated
by adding the natural numbers. So the 7th triangle
number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle
numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to
have over five divisors.

What is the value of the first triangle number to
have over five hundred divisors?
'''
divs = 0
a = 1000
tri = 0

def factors(test_num):
    a = 0
    for i in range(1, test_num + 1):
        if test_num%i == 0:
            a += 1
        if i > test_num/10:
            if a < 100:
                return 1

    return a

while divs <= 500:
    a += 1
    tri = tri + a
    divs = factors(tri)
    print(a, tri, divs)
    
print('''The first triangle number with over five
      hundred divisors is ''', tri)
