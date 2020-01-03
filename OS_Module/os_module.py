import os

print(os.getcwd())   # return cwd

# create folder(if folder is exist it will throw error)
# os.mkdir('operating system')

# check folder exist or not(return boolean)
# print(os.path.exists('operating system'))

# proper way to create folder
# if os.path.exists('operating system'):
#     print('already exist')
# else:
#     os.mkdir('operating system')

# create file
# open('file.txt', 'a').close()

# change working directory
# os.chdir(r'C:\New folder')

# listdir - return list of files and folder of 
# print(os.listdir())
# print(os.listdir(r'path of folder'))

# get path of every item in cwd or folder
# not a good way because that will change when os will change - linux - forward /
for item in os.listdir():
    # print(r'C:\Users\ts-pratik.kumar\Desktop\Python\OS_Module' + '\\' + item)
    path = os.path.join(os.getcwd(), item)
    print(path)