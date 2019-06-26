'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
start_num = str(2**1000)
end_num = []

for i in start_num:
    end_num.append(int(i))

print(sum(end_num))
