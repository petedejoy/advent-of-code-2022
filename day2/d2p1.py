# rock = a = 1
rock = 1
# paper = b = 2
paper = 2
# scissors = c = 3
scissors = 3

import pandas as pd

loss = 0
draw = 3
win = 6

# opening the file in read mode
my_file = open("./data.txt", "r")

# turn my_file into a dataframe
data = pd.read_csv(my_file, sep=" ", header=None, names = ['opponent', 'suggestion'])

data['opponent'] = data['opponent'].str.replace('A', '1')
data['opponent'] = data['opponent'].str.replace('B', '2')
data['opponent'] = data['opponent'].str.replace('C', '3')

# replace all occurances of x with a, y with b, and z with c in the "suggestion" column of my dataframe
data['suggestion'] = data['suggestion'].str.replace('X', '1')
data['suggestion'] = data['suggestion'].str.replace('Y', '2')
data['suggestion'] = data['suggestion'].str.replace('Z', '3')

# convert the "opponent" and "suggestion" columns to integers
data['opponent'] = data['opponent'].astype(int)
data['suggestion'] = data['suggestion'].astype(int)

# iterate through each row in data and calculate the score, adding the value of suggestion to each score
for index, row in data.iterrows():
    if row['opponent'] == row['suggestion']:
        data.at[index, 'score'] = draw + (row['suggestion'])
    elif row['opponent'] == 1 and row['suggestion'] == 3:
        data.at[index, 'score'] = loss + (row['suggestion'])
    elif row['opponent'] == 2 and row['suggestion'] == 1:
        data.at[index, 'score'] = loss + (row['suggestion'])
    elif row['opponent'] == 3 and (row['suggestion']) == 2:
        data.at[index, 'score'] = loss + (row['suggestion'])
    else:
        data.at[index, 'score'] = win + (row['suggestion'])

# sum up the scores
total_score = data['score'].sum()
print(total_score)