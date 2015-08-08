sum = 0
sequenceValue = 2
previousValue = 1

while sequenceValue < 4000000:
    if sequenceValue%2 == 0:
        sum += sequenceValue

    temp = sequenceValue

    sequenceValue += previousValue

    previousValue = temp

print(sum)
