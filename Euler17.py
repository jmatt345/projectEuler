'''
If the numbers 1 to 5 are written out in
words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters
used in total.

If all the numbers from 1 to 1000 (one
thousand) inclusive were written out in
words, how many letters would be used?
'''

from num2words import num2words

num = 0
words = []

for i in range(1, 1001):
    words.append(num2words(i))

for j in words:
    j = j.replace('-','')
    j = j.replace(' ','')
    num = num + len(j)
    
print(num)
