# fibonacci series
# 0 1 1 2 3 5 8    # first 2 term is fixed

def fibonacci_seq(n):
    a = 0
    b = 1
    for i in range(0,n):
        print(a, end = " ")
        next_term = a+b
        a = b
        b = next_term

num = int(input("enter the value of n : "))
fibonacci_seq(num)
