# readfile
# open function - to open the file
# read method  - read the file
# seek method  - to the position of the cursor
# tell method  - tell  the cursor position
# readline method - read single line
# readlines method - read file line by line
# close method - to close the file

f = open('file1.txt')              # open function take mode as a 2nd parameter('r'(default), 'w')
# we can also iterate f
for line in f:
    print(line, end='')

# print(f"cursor position - {f.tell()}")

# print(f.read())
# print(f.readline(), end='')
# print(f.readline())
# print(f.readline())
# print(f"cursor position - {f.tell()}")
# f.seek(0)
# print(f"cursor position - {f.tell()}")
# print(f.read())

# lines = f.readlines()[0:2]           # we can do slicing in readlines
# print(lines)
# for line in lines:
#     print(line, end='')

# data discriptor(name, closed)
print(f.name)                       # return name of the file
print(f.closed)                     # tell file is closed or not, return boolean
f.close()                          # best practice to close that file after any operation