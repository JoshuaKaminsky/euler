found = False

value = 20;

while not found:

    for index in range(1, 21):
        if value % index != 0:
            break

        if index == 20:
            found = True
            print(value)

    value += 20

