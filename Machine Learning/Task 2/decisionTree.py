import math

p = input("Value of p\n")
n = input("Value of n\n")

p = int(p)
n = int(n)
I = -p/(p+n)*math.log2(p/(p+n)) - n/(p+n)*math.log2(n/(n+p))
print(I)