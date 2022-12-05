import string
import pandas as p

# open the file in read mode
my_file = open("./data.txt", "r")
data = my_file.read()
# convert to a list on new lines
data = data.splitlines()
split_list = [data[x:x+3] for x in range(0, len(data),3)]
common_letters = []

# iterate through the items in split_list and determine what strings in each sublist have matching characters
for i in range(len(split_list)):
    # create a list of the common letters
    common_letter = []
    # iterate through each letter in the first string
    for j in range(len(split_list[i][0])):
        # if the letter is found in all three strings, add it to the list of common letters
        if split_list[i][0][j] in split_list[i][1] and split_list[i][0][j] in split_list[i][2]:
            common_letter += split_list[i][0][j]
    # print the common letters
    # print(common_letter)
    #de-duplicate the list of common letters
    common_letter = list(set(common_letter))
    common_letters.append(common_letter)

print(common_letters)
# convert each item in common_letters to a number based on its position in the alphabet
for i in range(len(common_letters)):
    for j in range(len(common_letters[i])):
        if common_letters[i][j] in string.ascii_lowercase:
            common_letters[i][j] = string.ascii_lowercase.index(common_letters[i][j])+1
        elif common_letters[i][j] in string.ascii_uppercase:
            common_letters[i][j] = string.ascii_uppercase.index(common_letters[i][j])+27


# convert common_letters to a list of integers
common_letters = [int(''.join(str(e) for e in common_letters[i])) for i in range(len(common_letters))]

#sum the integers in common_letters
print(sum(common_letters))

    

