# read file normally
# f = open('file.txt')
# f.read()
# f.close()

# with block(context manager)

with open('file1.txt') as f:  # using block we don't need to close file or any other thing
    data = f.read()
    print(data)

print(f.closed)