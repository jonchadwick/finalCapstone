#This grid is the original input that is displayed in "task 15".

grid = [["-", "-", "-", "#", "#"], 
        ["-", "#", "-", "-", "-"], 
        ["-", "-", "#", "-", "-"], 
        ["-", "#", "#", "-", "-"], 
        ["-", "-", "-", "-", "-"]]

def minesweeper(grid):
    
#This line checks the amount of rows within the input grid   
    
    rows = len(grid)

#This line checks the amount of columns needed by taking the first row "[0]" and checks the amount of elements within the list.

    cols = len(grid[0])
    
#Here now creates a new grid the same as the input and replaces all positions with "0"    
    
    result = [["0"] * cols for _ in range(rows)]
    
#This nested for loop loops over each row and each position within the grid, assigning a # to the result table when found from the input.

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "#":
                result[r][c] = "#"
                continue

#Initialise a count of 0.

            count = 0

#This for loop checks each position around the current position to check for the # symbol using the axis point in the brackets. 

            for x, y in ((r-1, c-1), (r-1, c), (r-1, c+1),
                         (r, c-1), (r, c+1),
                         (r+1, c-1), (r+1, c), (r+1, c+1)):

#This line of code checks that the adjacent cells are not going out of bounds of the grid.

                if x < 0 or x >= rows or y < 0 or y >= cols:
                    continue

#This if statement checks that if the position being checked is a # symbol then the count is increased by 1.

                if grid[x][y] == "#":
                    count += 1
            result[r][c] = str(count)
            
    return result

print(minesweeper(grid))