# Hour hand turned by α degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour. Input and output in this problems are floating-point numbers.

alpha = float(input())

minute_angle = (alpha % 30) * 12
print(minute_angle)
