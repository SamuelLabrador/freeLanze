import numpy as np

#initialize array 
A = np.array([4, 5, 17, 23, 11, 2])

#get size of array
sz = len(A)

#initialize table
Table = np.zeros((sz, sz))

#T is the sum we are trying to find
T = 44

#keep track of whether or not sum was found
flag = 0

for i in range(sz): #start from left most, move to right column
	for j in range(i, -1, -1): #move UP rows (bottom up)
		
		#if the indecies are equal, 
		if j == i:
			# if column is greater than the target, set td = 0
			if A[i] > T:
				Table[j, i] = 0
			#else, set the td to the column
			else:
				Table[j, i] = A[i]

		else:
			val = 0
			#get the PREVIOUS largest value that can be added to the current row
			for k in range(j + 1, i + 1, 1):
				#check if the value is the largest
				if Table[k, i] + A[j] <= T and Table[k, i] + A[j] > val:
					val = Table[k, i] + A[j]
					
					#check whether the target was found
					if(val == T):
						flag = 1

			#set td to that value
			Table[j, i] = val

#check if value was found
if flag:
	print('True')
else:
	print('False')

#output stuff
print('looking for {}'.format(T))
print(A)
print(Table) 

