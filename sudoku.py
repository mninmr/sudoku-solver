## Insight Data Engineering Fellows Program Coding Challenge
## Input: sudoku.csv 
## Output: solved.csv

def from_file(file):
	return [line.strip().split(',') for line in open(file)]

def to_file(puzzle):
	with open('solved.csv', 'w') as f:
		for row in puzzle:
			for char in row:
				f.write(char)
				if char == row[-1]:
					f.write('\n')
				else:
					f.write(',')
	f.close()

def solve(puzzle, row, col):
	if row == 9 and col == 0:
		to_file(puzzle)
	elif col == 9:
		pass
	else:
		if puzzle[row][col] is not '0':
			solve(puzzle, row, col+1)
			if col == 8:
				solve(puzzle, row+1, 0)
		else:
			for num in range(1, 10):
				if checkLegal(puzzle, row, col, chr(ord('0')+num)):
					puzzle[row][col] = chr(ord('0')+num)
					solve(puzzle, row, col+1)
					if col == 8:
						solve(puzzle, row+1, 0)
					puzzle[row][col] = '0'

def checkLegal(puzzle, row, col, target):
	for ii in range(0, 9):
		if puzzle[row][ii] == target:
			return False
	for ii in range(0, 9):
		if puzzle[ii][col] == target:
			return False
	startRow = (row/3)*3
	startCol = (col/3)*3
	for ii in range(startRow, startRow+3):
		for jj in range(startCol, startCol+3):
			if puzzle[ii][jj] == target:
				return False
	return True

def main():

	puzzle = from_file('sudoku.csv')	
	solve(puzzle, 0, 0)

if __name__ == '__main__':
	main()