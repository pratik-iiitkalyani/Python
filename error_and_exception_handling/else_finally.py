# else finally clause in exception handling

while True:
    try:
        number = int(input('enter a number: '))
    except ValueError:
        print('you didn\'t entered integer')
    except:
        print('unexpected error..')
    else:                                         # excuted when no exception occur or try block excuted successfully
        print(f"user input = {number}")
        break

    finally:                                       # excuted every time
        print('finally block...')

# finally is used when we want to release our database after performing some task
