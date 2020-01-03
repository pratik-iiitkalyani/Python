import pdb     # import pdb module

# debugging - find error in code and fix that error

# why debugging?
# 1). our program is not running and causing unexpected errors
# 2). our program is working fine but not working the same way we want

# step for debugging
# 1). set trace
# 2). execute code line by line

pdb.set_trace()# use where you want        # excute code line by line
# (Pdb) l                                  # tell where your code is stopped
# (Pdb) n                                  # line will we be excute
# (Pdb) c                                  # code will excuted normally
# (Pdb) q                                  # for quiting

name = input('please type your name : ')
age = input('please type your age : ')
print(f"hello {name} your age is {age}")
age2 = age + 5
print(f"{name} you will be {age2} in next five year") 