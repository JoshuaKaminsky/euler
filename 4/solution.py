def is_palindrome(value):
    reversed = (int)(str(value)[::-1])
    return value == reversed

x = 100
y = 100
max_palindrome = 0
max_x = 0
max_y = 0

while x < 1000:
    while y < 1000:
        z = x*y
        if is_palindrome (z):

            if max_palindrome < z:
                max_palindrome=z
                max_x = x
                max_y = y

        y += 1

    x += 1
    y = 100

print (max_palindrome)
print (max_x)
print (max_y)