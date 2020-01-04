# define a fun which takes a number(n)
# and return a dict containing cube of n from 1 to n
def cubeFinder(n):
    dict = {}
    for i in range(1,n+1):
        dict[i] = i*i*i
    return dict
print(cubeFinder(5))