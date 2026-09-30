import math
result = 1.0

for n in range(1,21):
    numerator = n**(0.65*n)
    denominator=2*(n**2)+ math.factorial(n-1)
    term = (numerator/denominator)*math.cos(n/math.pi)
    result *= term

print(result)