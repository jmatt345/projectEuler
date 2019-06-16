# Find the largest palindrome made from the product of two 3-digit numbers.

# create two 3-digit numbers
a = 101
dromes = []

while a < 1000:
    b = 101
    while b < 1000:
        product = str(int(a*b))
        revProduct = reversed(product)
        if list(product) == list(revProduct):
            dromes.append(int(product))
        b+=1
    a+=1

dromes.sort(reverse = True)
print(dromes[0])
