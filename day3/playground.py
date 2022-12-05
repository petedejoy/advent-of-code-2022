string = "hello"
string2 = "hell"

result = ''

# find the common characters between string and string2
for i in range(len(string)):
    if string[i] in string2:
        result += string[i]

print(result)