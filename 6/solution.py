
sum = 0
squaresum = 0

for index in range(1, 101):
    sum += index
    squaresum += index * index

print(sum)

print(squaresum)

sumsquared = sum * sum

print(sumsquared)

print(sumsquared - squaresum)
