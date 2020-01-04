def wordCounter(string):
    count = {}
    for i in string:
        count[i] = string.count(i)
    return count
str = 'aaa'
print(wordCounter(str))