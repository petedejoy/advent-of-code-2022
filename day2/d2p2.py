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
data = pd.read_csv(my_file, sep=" ", header=None, names = ['opponent', 'outcome'])

data['opponent'] = data['opponent'].str.replace('A', 'rock')
data['opponent'] = data['opponent'].str.replace('B', 'paper')
data['opponent'] = data['opponent'].str.replace('C', 'scissors')

# replace all occurances of x with a, y with b, and z with c in the "outcome" column of my dataframe
data['outcome'] = data['outcome'].str.replace('X', 'lose')
data['outcome'] = data['outcome'].str.replace('Y', 'draw')
data['outcome'] = data['outcome'].str.replace('Z', 'win')

# convert the "opponent" and "outcome" columns to integers
# data['opponent'] = data['opponent'].astype(int)


# iterate through each row in data and calculate the score, adding the value of outcome to each score
for index, row in data.iterrows():
    if row['outcome'] == 'draw':
        data.at[index, 'move'] = data.at[index, 'opponent']
    elif row['opponent'] == 'paper' and row['outcome'] == 'lose':
        data.at[index, 'move'] = 'rock'
    elif row['opponent'] == 'paper' and row['outcome'] == 'win':
        data.at[index, 'move'] = 'scissors'
    elif row['opponent'] == 'rock' and row['outcome'] == 'lose':
        data.at[index, 'move'] = 'scissors'
    elif row['opponent'] == 'rock' and row['outcome'] == 'win':
        data.at[index, 'move'] = 'paper'
    elif row['opponent'] == 'scissors' and row['outcome'] == 'lose':
        data.at[index, 'move'] = 'paper'
    elif row['opponent'] == 'scissors' and row['outcome'] == 'win':
        data.at[index, 'move'] = 'rock'

#add a column called move_integer to the dataframe, translate to ints
data['move_integer'] = data['move']
data['move_integer'] = data['move_integer'].str.replace('rock', '1')
data['move_integer'] = data['move_integer'].str.replace('paper', '2')
data['move_integer'] = data['move_integer'].str.replace('scissors', '3')
data['move_integer'] = data['move_integer'].astype(int)

# iterate through each row in data and calculate the score, adding the value of outcome to each score
for index, row in data.iterrows():
    if row['outcome'] == 'draw':
        data.at[index, 'score'] = draw + (row['move_integer'])
    elif row['outcome'] == 'lose':
        data.at[index, 'score'] = loss + (row['move_integer'])
    elif row['outcome'] == 'win':
        data.at[index, 'score'] = win + (row['move_integer'])

# sum up the scores
total_score = data['score'].sum()
print(total_score)