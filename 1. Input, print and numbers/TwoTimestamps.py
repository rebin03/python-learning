# A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them. The moment of the first timestamp occurred before the moment of the second timestamp.

 h1 = int(input())
 m1 = int(input())
 s1 = int(input())
 
 h2 = int(input())
 m2 = int(input())
 s2 = int(input())
 
 t1 = (h1*60*60)+(m1*60)+s1
 t2 = (h2*60*60)+(m2*60)+s2
 
 timestamps = t2-t1
 print(timestamps)
 