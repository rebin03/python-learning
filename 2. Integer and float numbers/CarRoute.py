# A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.

N = int(input())
M = int(input())

days = M // N  
if M % N != 0: 
    days += 1 

print(days)