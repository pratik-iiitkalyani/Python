# read from file1.txt and write on file2.txt
with open('file1.txt', 'r') as rf:
    with open('file2.txt', 'w') as wf:
        wf.write(rf.read())