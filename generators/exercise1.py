# define generator function
# take one number as argument
# generate a sequence of even numbers form 1 to that number

def even_num(num):
    for num in range(1, num+1):
        if num%2 == 0:
            yield(num)
even_nums = even_num(10)

for i in even_nums:
    print(i)

def even(num):
    for i in range(2, num+1, 2):
        print(i)

even(10)