# Exception handling
# try except else finally
# Exception - error that comes during excution time

# age = int(input('enter your age: '))  # user enter seven
# if age < 18:
#     print('you can\'t play this game')
# else:
#     print('you can play this game')

while True:
    try:
        age = int(input('enter your age: '))
        break
    except ValueError:       # best practise(decrease the complexity)
        print('may be you entered string instead of number, try again')
    except: # if not value error then this block will we excuted
        print('unexpected error..')
    

if age < 18:
    print('you can\'t play this game')
else:
    print('you can play this game')