import os
import shutil

# os.walk()   # give complete file and folder of given path - return generator
# os.chdir(r'C:\Users\ts-pratik.kumar\Desktop\Python')
# fileiter = os.walk(r'C:\Users\ts-pratik.kumar\Desktop\Python')
# for current_path, folder_names, file_names in fileiter:
#     print(f"current_path : {current_path}")
#     print(f"folder_names : {folder_names}")
#     print(f"file_names : {file_names}")


# delete folder
# os.rmdir('operating system')    # delete folder only when folder is empty

# create folder inside folder
# os.makedirs('operating system/new folder')


# delete folder when folder is empty or not
# shutil.rmtree('operating system')     # delete permanently

# copy folder to another folder
# shutil.copytree('new', 'newfolder/new1')

# copy file 
# shutil.copy('file.txt', 'documents/file.txt')

#move the file
# shutil.move('file.txt', new/file2.txt)

# move folder
# shutil.move('new', 'documents/new2')
