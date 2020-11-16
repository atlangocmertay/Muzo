x = float(input('write a number: '))
if x >= 5:
    y = x ** 2 + 3
elif x < 5 and x > 0:
    y = x ** 0.5
else:
    y = 0
print(float(y))
