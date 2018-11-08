import numpy as np

def func():
	dimensions = (20, 20)
	A = np.random.randint(2, size=(dimensions))
	# A = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
	# A = np.array([[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]])
	# A = np.ones(dimensions)
	Table = np.zeros(dimensions)

	#m corresponds to rows, n corresponds to columns
	(m, n) = A.shape 

	largestSquare = 0

	for i in range(m): #go through row first
		for j in range(n): #go through each corresponding column
			aboveCell = 0
			leftCell = 0
			cornerCell = 0

			currentCell = int(A[i, j])

			#get data cell above
			if i != 0:
				aboveCell = int(Table[i - 1, j])

			#get data cell to the left
			if j != 0:
				leftCell = int(Table[i, j - 1])

			#get the corner data cell
			if j != 0 and i != 0:
				cornerCell = int(Table[i - 1, j - 1])		
			

			if aboveCell != 0 and leftCell != 0 and currentCell != 0:
				#if both cells are greater than 0 and equal set current cell to cell_left + 1
				if aboveCell == leftCell and aboveCell == cornerCell:
					Table[i, j] = Table[i - 1, j] + 1
				#else if both cells are greater than 0 and not equal, take the larger of the two cells

				elif aboveCell >= leftCell:
					Table[i, j] = aboveCell
				elif leftCell > aboveCell:
					Table[i, j] = leftCell
				else:
					Table[i, j] = 1

				if (aboveCell == 1 or leftCell == 1) and Table[i, j] > 2:
					Table[i, j] = 1
			#else current cell = 0
			else:
				Table[i, j] = currentCell

			#if currentCell**2 > largest square, largestSquare = currentCell**2 
			if Table[i, j]**2 > largestSquare:
				largestSquare = Table[i, j]**2
	return largestSquare, A

x = 0
# while x < 25:
# 	(x, y) = func()
(x, y) = func()
print(x)
print(y)