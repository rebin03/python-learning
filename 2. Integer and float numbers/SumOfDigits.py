# Given a three-digit number. Find the sum of its digits.

a = int(input())

n1 = a%10
n2 = a//10%10
n3 = a//100

print(n1+n2+n3)