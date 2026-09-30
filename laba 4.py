import math

total_sum = 0.0

for n in range(1,31):
    numerator=(math.pi / 2)**n
    denominator = math.factorial(2*n+1)
    term = n*(numerator/denominator)*math.sin(n)
    total_sum += term

    print(total_sum)
