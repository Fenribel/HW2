import math
def my_tan(x):
    term = x
    sum = x
    eps = 10 ** (-8)
    B = [1]
    for n in range(150):
        n += 1
        b = 0
        npofact = math.factorial(n + 1)
        kpofact = 1
        for i in range(n):
            i += 1
            kpofact *= (i + 1)
            b += B[n - i] * (-1) * npofact / ((n + 1) * (kpofact * math.factorial(n - i)))
        B.append(b)
    n = 1

    while abs(term) > abs(sum * eps) and n < 50:
       n += 1
       term = B[2 * n]/B[2 * n - 2] * (-4) * (1 - 4 ** n)/(1 - 4 ** (n - 1)) * term * x ** 2 / ((2 * n ) * (2 * n - 1))
       sum += term
    print(n)
    return sum

x = 0
while (True):
    x+= 0.025
    if (math.tan(x) != 0):
        print ("x = ", x, "    ", abs ((my_tan(x) - math.tan(x))/(math.tan(x))))
    else:
        print ("tan(x) = 0, my_tan(x) = ", my_tan(x))