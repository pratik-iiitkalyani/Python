print("Hello \"world\" World")       #single quotes
print('pratik \'kumar\' kumar')      #double quotes
print("line A")
print("line B")
print("line A\nline B\n line C") # \n for new line
print("this is a backslash\\")   # for printing \
print("this is a double backslash\\\\") # for printing \\

# escape char as a normal text
#output: line A \n line B
print("line A \\n line B")
print("line A \\t line B")
print("this is 2 backslash \\\\")
print("this is 4 backslash \\\\\\\\")
#output: \" \'
print("\" \'")   #output-" '
print("\\\" \\\'")
# \' - ' (b)
# \\ - \ (a)
# \\\' - \'code

# escape char as a normal text:shortcut
#output: line A \n line B
print(r"line A \n line B")
print(r"line A \t line B")
print(r"this is 2 backslash \\")
print(r"this is 4 backslash \\\\")
#output: \" \'
print(r"\" \'")  #raw string
print("\\\" \\\'")