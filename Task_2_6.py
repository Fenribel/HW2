import math

def my_tan(x):
    while abs(x) > math.pi/2:
        if x > 0:
            x -= math.pi
        else:
            x += math.pi
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

while (True):
    try:
        x = float(input())
    except:
        print ("Exit")
        break
    if (math.tan(x) != 0):
        print (abs ((my_tan(x) - math.tan(x))/(math.tan(x))), my_tan(x + 2*math.pi) - my_tan(x))
    else:
        print ("tan(x) = 0, my_tan(x) = ", my_tan(x))