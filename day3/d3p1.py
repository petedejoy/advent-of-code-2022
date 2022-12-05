import string
import pandas as p

# open the file in read mode
my_file = open("./data.txt", "r")
data = my_file.read()
# convert to a list on new lines
data = data.splitlines()

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

#create a dataframe with two columns
df = p.DataFrame(columns=['c1', 'c1num', 'c2', 'c2num', 'common_letters', 'common_letters_num'])

# iterate through each string in data
for i in range(len(data)):
    # set the first half of the string to first_half
    first_half  = data[i][:len(data[i])//2]
    # add the value of first_half to the first column of the dataframe
    df.at[i, 'c1'] = first_half
    # set the second half of the string to second_half
    second_half = data[i][len(data[i])//2:]
    # add the value of second_half to the second column of the dataframe
    df.at[i, 'c2'] = second_half


# find the common characters between the strings in c1 and c2
for index, row in df.iterrows():
    # create a list of the common letters
    common_letters = []
    # iterate through each letter in the first string
    for i in range(len(row['c1'])):
        # if the letter is in the second string, add it to the list of common letters
        if row['c1'][i] in row['c2']:
            common_letters.append(row['c1'][i])
        # de-duplicate the list of common letters
        common_letters = list(set(common_letters))
    # add the list of common letters to the dataframe
    df.at[index, 'common_letters'] = common_letters


# convert the items in common_letters to numbers based on their position in the alphabet
for index, row in df.iterrows():
    common_letters_num = []
    # iterate through each letter in the first string
    for i in range(len(row['common_letters'])):
        # if the letter is in the second string, add it to the list of common letters
        if row['common_letters'][i] in lowercase:
            common_letters_num.append(lowercase.index(row['common_letters'][i])+1)
        elif row['common_letters'][i] in uppercase:
            common_letters_num.append(uppercase.index(row['common_letters'][i])+27)
    # convert common_letters_num to a string
    common_letters_num = ''.join(str(e) for e in common_letters_num)
    # add the list of common numbers to the dataframe
    df.at[index, 'common_letters_num'] = common_letters_num

# convert common_letters_num elements to integers
df['common_letters_num'] = df['common_letters_num'].astype(int)
# sum the total of common_letters_num
total = df['common_letters_num'].sum()
print(total)
