# @calculate_time
# def fun():
#     print("dafjh")
# fun()

# output - this fun took 3 sec to run
from functools import wraps
import time

def calculate_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"excuting......{function.__name__} function")
        t1 = time.time()
        returned_value = function(*args, **kwargs)
        t2 = time.time()
        print(f"this function took {t2-t1} sec to run")
        return returned_value
    return wrapper


@calculate_time
def square(n):
    return [i**2 for i in range(1, n+1)]

print(square(500))
