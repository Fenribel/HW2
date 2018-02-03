from math import *
from tkinter import *

def my_tan(x):
    term = x
    sum = x
    eps = 10 ** (-8)
    B = [1]
    for n in range(150):
        n += 1
        b = 0
        npofact = factorial(n + 1)
        kpofact = 1
        for i in range(n):
            i += 1
            kpofact *= (i + 1)
            b += B[n - i] * (-1) * npofact / ((n + 1) * (kpofact * factorial(n - i)))
        B.append(b)
    n = 1

    while abs(term) > abs(sum * eps) and n < 50:
        n += 1
        term = B[2 * n] / B[2 * n - 2] * (-4) * (1 - 4 ** n) / (1 - 4 ** (n - 1)) * term * x ** 2 / (
                (2 * n) * (2 * n - 1))
        sum += term
    return sum

def err(x):
    if (tan(x) != 0):
        return abs((my_tan(x) - tan(x))/tan(x))
    else:
        return 0



root = Tk()

x_0 = 10**(2)
y_0 = 10**(3)
x_sc = 10**(0)

canv = Canvas(root, width = 1000, height = 1000, bg = "white")
canv.create_line(500, 1000, 500, 0, width = 2, arrow = LAST)
canv.create_line(0, 500, 1000, 500, width = 2, arrow = LAST)
canv.create_text(980, -20 +500, font = ("Purisa", 18), text = "x", fill = "purple")
canv.create_text(-57 + 500, 25, font = ("Purisa", 15), text = "err*" + str(x_sc), fill = "purple")

First_x = -500



for i in range(16000):
    if (i % 800 == 0):
        k = First_x + (1 / 16) * i
        canv.create_line(k + 500, -3 + 500, k + 500, 3 + 500, width=0.5, fill='black')
        canv.create_line(k + 500, 0, k + 500, 1000, width=0.1, fill='grey', dash=(1, 1))
        canv.create_text(k + 515, 10 + 500, font = ("Purisa", 10), text=str(k/x_0), fill="purple")
        if (k != 0):
            canv.create_line(-3 + 500, k + 500, 3 + 500, k + 500, width=0.5, fill='black')
            canv.create_line(0, k + 500, 1000, k + 500, width=0.1, fill='grey', dash=(1, 1))
            canv.create_text(25 + 500, k + 500 + 20, font = ("Purisa", 10), text=str(-k/y_0*x_sc), fill="purple")
    try:
        x = First_x + (1 / 16) * i
        y = -err(x/x_0)*y_0 + 499
        x += 499
        canv.create_oval(x, y, x + 1, y + 1, fill='black')
        if i % 1600 == 0:
            print(i/1600)
    except:
        First_x = -500


canv.pack()
root.mainloop()