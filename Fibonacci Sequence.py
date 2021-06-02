# Write a program to ask the user how many Fibonacci numbers to print
def fib(n):
    a = 1
    b = 1

    if n == 1:
        print(a)
    else:
        print(a, end=',')
        print(b, end=',')
        for i in range(2, n):
            c = a+b
            a = b
            b= c
            print(c, ',', sep='', end='')


fib(int(input('Enter a number: ')))