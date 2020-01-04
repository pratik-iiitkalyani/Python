#replace method
string = "she is beautiful and she is good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was"))
print(string.replace("is","was",1))  # first is changed

#find method()
print(string.find("is"))
print(string.find("is",5)) #we are starting from index num 2

is_pos1= string.find("is")
is_pos2= string.find("is",is_pos1+1)
print(is_pos2)