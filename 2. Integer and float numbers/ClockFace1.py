# H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle (in degrees) of the hour hand on the clock face right now.

H = int(input())
M = int(input())
S = int(input())

hour_angle = (H % 12 + M / 60 + S / 3600) * 30
print(hour_angle)
