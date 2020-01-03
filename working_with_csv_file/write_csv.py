# name, country
# pratik, India
# mohit, Japan
# ben, Germany

# writer, DictWriter

from csv import writer, DictWriter

#using writer
with open('file1.csv', 'w', newline='') as f:
    csv_writer = writer(f)
    # method to write - writerow, writerows
    # using writerow
    # csv_writer.writerow(['name', 'country'])
    # csv_writer.writerow(['pratik', 'India'])
    # csv_writer.writerow(['mohit', 'Japan'])

    #using writerows(list of lists)
    csv_writer.writerows([['name', 'country'], ['pratik', 'India'], ['mohit', 'Japan']])


# using DictWriter(in DictWriter we have to specify header)
with open('file2.csv', 'w', newline='') as f:
    csv_writer = DictWriter(f, fieldnames=['first_name', 'last_name', 'age'])
    csv_writer.writeheader()    # write headers
    # method to write - writerow, writerows
    # using writerow
    # csv_writer.writerow({
    #     'first_name': 'pratik',
    #     'last_name': 'kumar',
    #     'age': 23
    # })
    # csv_writer.writerow({
    #     'first_name': 'mohit',
    #     'last_name': 'kumar',
    #     'age': 23
    # })

    #using writerows(list of lists)
    csv_writer.writerows([
        {
        'first_name': 'pratik',
        'last_name': 'kumar',
        'age': 23
        },
        {
        'first_name': 'mohit',
        'last_name': 'kumar',
        'age': 23
        },
        {
        'first_name': 'amit',
        'last_name': 'kumar',
        'age': 23
        }
    ])
