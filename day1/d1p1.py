from itertools import groupby

# opening the file in read mode
my_file = open("./data.txt", "r")
  
# reading the file
data = my_file.read()
## turn my_file into a list of lists on new lines
    
data = data.splitlines()

## create separate lists on empty strings in list
temp_idx = data.index('')
res = [list(sub) for ele, sub in groupby(data, key = bool) if ele]

## Sum the elements of each sublist in res
res = [sum(map(int, sub)) for sub in res]

## Find the highest number in res
print(max(res))

my_file.close() 