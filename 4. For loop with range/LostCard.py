# There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards.
# Given a number N, followed by N − 1 integers - representing the numbers on the remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.

N = int(input())

rc = []
for i in range(N - 1):
    cn = int(input())
    rc += [cn]

lc = None
for cn in range(1, N + 1):
    found = False
    for j in range(N - 1):
        if cn == rc[j]:
            found = True
            break
    if not found:
        lc = cn
        break

print( lc)
