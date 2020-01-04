user = {}

name = raw_input('enter your name : ')
age = input('enter your age : ')
fav_movie = raw_input('enter your fav movie seperated by ,').split(",")
fav_song = raw_input('enter your fav song seperated by ,').split(",")

user['name'] = name
user['age'] = age
user['fav_movie'] = fav_movie
user['fav_song'] = fav_song
# print(user)

for key, value in user.items():
    print('{} : {}'.format(key, value))