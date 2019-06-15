multiples = []

for i in range(100):
    if i%3 == 0:
        multiples.append(i)
        continue
    if i%5 == 0:
        multiples.append(i)

print(sum(multiples))
