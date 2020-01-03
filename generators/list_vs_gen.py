# list vs generators
# memory usages and time
# when to use list and when to use generators
import time
# memory
# l = [ i**2 for i in range(10000000)]  # 10 M   takes approx 400 MB

# g = (i**2 for i in range(10000000))  # 10 M      small kb

# time
t1 = time.time()
l = [ i**2 for i in range(10000000)]  # takes approx 6 s
t2 = time.time()
print(t2-t1)

t1 = time.time()
g = (i**2 for i in range(10000000))      # takes fraction of second
t2 = time.time()
print(t2-t1)

# list - when we want performe operation on data again and again(like todo list)
# generators - for single time use