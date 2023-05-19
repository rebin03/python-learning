# A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

d = int(input())
c = int(input())
num = int(input())

dlr = num*d
cnt = num*c

a = cnt//100
cent = cnt%100

dollar = dlr+a

print(dollar, cent)