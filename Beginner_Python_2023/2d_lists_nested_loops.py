
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][1]) #how to access the lists

#for nested for loops
for row in number_grid:
    for col in row:
        print(col)
        #for every item in the colum
        #and every column in the row
        #individually print the item