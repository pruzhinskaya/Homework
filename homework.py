#!/usr/bin/env python3

def isint(n):
    return int(n) == float(n)

# Fibonacci
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
        return a[n-1]
    else:
        print("ay-ay-ay, n must be natural")

# Factorial 1
def factorial(n):
    if isint(n) and n >= 0:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return n*factorial(n-1)
    else:
        print("ay-ay-ay, n must be natural or zero")


if __name__ == '__main__':
    print("The first Fibonacci number is ", Fibi(1))
    print("The 2018 Fibonacci number is ", Fibi(2018))
    print("Factorial of 5000 is ", factorial(5000))

# Vpechatleniya: it's the most amazing function I've ever seen!
