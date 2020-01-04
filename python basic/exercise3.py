user_name, char = input("enter the name and character : ").split(",")
print(f"lenght of the user_name is {len(user_name)}")
print(f"character count : {user_name.count(char)}")  #case sensitive
print(f"character count : {user_name.lower().count(char.lower())}")
# in above space is also counted
#method in which space are not counted
#   "Pratik"  --->"Pratik"--->"pratik"
#"  A "----->"A"--->"a"
# user_name.strip().lower().count(a)
# a=char.strip().lower()
# print(f"character count : {user_name.lower().count(char.strip().lower())}")