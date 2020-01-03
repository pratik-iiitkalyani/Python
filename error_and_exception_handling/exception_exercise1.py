# make a function 'divide'
# divide(a, b)

# print(divide(4, 2))  # 2
# print(divide(4, 0))  # please don't divide by zero
# print(divide('4', 2)) # please input number only

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as err:
        # print('you can not divide a number by zero')
        print(err)
    except TypeError as err:
        print('numbers must be int or float')
        # print(err)
    except:
        print('unexpected error')

print(divide(4, '2'))
    