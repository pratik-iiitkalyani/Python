# write a function so that we can return square, cube, 4th power.....of given number

def to_power(x):
    def cal_power(n):
        return n**x
    return cal_power

cube = to_power(3)
print(cube(4))

square = to_power(2)
print(square(4))