# An Automorphic number is a number whose square ends with the same number itself.

# If a number n is squared (n * n) and the last digits of the result are exactly n, then it is an Automorphic number.



n = int(input())

sq = n * n

if sq % 100 == n:   # check last digits
    print("Automorphic Number")
else:
    print("Not Automorphic")