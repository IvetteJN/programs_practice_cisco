'''
Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

Your task is to write a program which:

*reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
*outputs Yes if the Sudoku is valid, and No otherwise.
'''

#A function that checks whether a list passed as an argument contains nine digits from '1' to '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]

# A list of rows representing the sudoku.
rows = [ ]
for r in range(9):
    ok = False
    while not ok:
        row = input("Enter row #" + str(r + 1) + ": ")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Incorrect row data - 9 digits required")
    rows.append(row)

ok = True

# Check if all rows are good.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Check if all columns are good.	
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Check if all sub-squares (3x3) are good.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Make a string containing all digits from a sub-square.
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

# Print the final verdict.
if ok:
    print("Yes")
else:
    print("No")
    

'''
Test data:
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672

195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
'''