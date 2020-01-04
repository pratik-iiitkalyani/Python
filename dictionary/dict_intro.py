# create dictionaries
# 1st method
# user = {'name':'pratik','age':22}
# print(user)
# print(type(user))


# 2nd method
user = dict(name = 'pratik',age=24)
print(user)

# accessing data
print(user['name'])
print(user['age'])


#  dictionary can store any type of data type
user_info = {
    'name':'pratik',
    'age':24,
    'fav_movie':['3 idiot','fan'],
    'fav_sports':['cricket','football']
}
print(user_info['fav_movie'])

# add data to empty dictionary
user_info2 = {}
user_info2['name'] = 'raja'
user_info2['age'] = 22
print(user_info2)