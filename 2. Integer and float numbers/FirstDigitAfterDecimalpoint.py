# Given a positive real number, print its first digit to the right of the decimal point.

num = float(input())
d = num - int(num)
f = int(d * 10)
print(f)
