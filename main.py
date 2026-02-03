
#1-masala
a = [12, 10, 20, 9]
b = [13, 9, 20]

result = set(a) - set(b)
print(result)

#2-masala

raqamlar = {1, 2, 3, 4, 5, 6, 7}

kvadrad = {x**2 for x in raqamlar if (x**2) % 2 == 0}

print(kvadrad)

#3-masala

numbers = {1, 3, 5, 7, 9, 11, 13}
minimum = 5
maximum = 11

result = set()

for x in numbers:
    if x >= minimum and x <= maximum:
        result.add(x)

print(result)

