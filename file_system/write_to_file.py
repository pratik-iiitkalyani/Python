# 'r' - for reading the file(default mode)
# 'w', 'a' and 'r+' for reading the file 

# with open('file1.txt', 'r') as f:
#     data = f.read()
#     print(data)

# w mode override the content of the file, if file1.txt is not present it will
#  create and write it
# generally used while working with empty file
# with open('file.txt', 'w') as f:
#     f.write("hello")


# a(append) mode - append content it the last(not delete the content of the file) 
# it also create the file if file is not present
# with open('file.txt', 'a') as f:
#     f.write("\nhello")

# r+(read and write) - it will create file if file is not present
# it will override from starting point
# if we want to append usnig r+ we have to change to cursor position using seek method
with open('file1.txt', 'r+') as f:
    f.seek(len(f.read()))
    f.write("\nhello")