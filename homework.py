#!/usr/bin/env python3

# Fibonacci
def isint(n):
    return int(n) == float(n)


def Fibi(n):
    if isint(n) and n>0:
        a = []
        for i in range(n):
            if i == 0:
                a.append(0)
            elif i == 1:
                a.append(1)
            else:
                c = a[i-1] + a[i-2]
                a.append(c)
        print(a[n-1])
    else:
        print("ay-ay-ay, n must be natural")

# Factorial
def factorial(n):
    if isint(n) and n >= 0:
        if n == 0:
            print(1)
        else:
            c = 1
            for i in range(n):
                c = c*(i+1)
            print(c)
    else:
        print("ay-ay-ay, n must be natural or zero")

if __name__ == '__main__':
    print(Fibi(1), Fibi(2018), factorial(5000))

# Vpechatleniya: it's the most amazing function I've ever seen!
