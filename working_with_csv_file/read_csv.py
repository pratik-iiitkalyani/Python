# read using reader
from csv import reader, DictReader

# with open('file.csv', 'r') as f:
#     csv_reader = reader(f)       # reader return iterator object
#     # print(type(csv_reader))
#     next(csv_reader)             # remove the heading
#     for i in csv_reader:
#         print(i)

# read using DicReader

# return ordered dict
with open('file.csv', 'r') as f:
    csv_reader = DictReader(f)
    # csv_reader = DictReader(f, delimiter='|')  if text seperated by |
    for row in csv_reader:
        # print(row)
        print(row['name'])       