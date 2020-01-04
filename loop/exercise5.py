# name  = input("enter the name:")
# dict_of_string = {}
# for each_char_number in range(len(name)):
#     if dict_of_string.get(name[each_char_number]):
#         dict_of_string.update({name[each_char_number]: dict_of_string.get(name[each_char_number]) + 1})
#     else:
#         dict_of_string.update({name[each_char_number]: 1})
# print(dict_of_string)

name = input("enter the namr :")
i = 0
temp = ""
while i < len(name):
    if name[i] not in temp:
        temp = temp+name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i = i+1