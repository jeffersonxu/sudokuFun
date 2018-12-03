file_name = input("What is the name of the Sudoku txt file? ")

with open(file_name) as f:
    lines = [line.rstrip('\n') for line in f]

#9 digits for every box, 81 boxes, 729 variables

#horizontal
row = 1
for line in lines: 
	digits = line.split()
	for digit in digits:
		if int(digit) != 0:
			print("Every other digit in row:", row, " cannot equal", digit)

#vertical
for line in lines: 
	digits = line.split()
	col = 1
	for digit in digits:
		if int(digit) != 0:
			print("Every other digit in column:", col, " cannot equal", digit)
		col+=1



#3x3 boxes