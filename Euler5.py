'''
What is the smallest positive number that
is evenly divisible by all of the numbers
between 1 and 20?
'''

test_num = 0
test_multiple = 1
hi_div = 10

while True:
    test_num += test_multiple 
    div = hi_div

    while div < 21:
        if test_num%div == 0:
            div += 1
            hi_div = div
            test_multiple = test_num
        else:
            break
    if div == 21:
        break
                
print(test_num)
