# read from file1.txt
# Harshit,100
# Mohit,50
# Aaditya,200
# Nitish,500

# and write on file2.txt as
# Harshit salary is 100

with open('file1.txt', 'r') as rf:
    with open('file2.txt', 'w') as wf:
        for line in rf.readlines():
            name, salary = line.split(',')
            wf.write(f"{name}\'s salary is {salary}")