import numpy as np 

A = np.array([4, 5, 17, 23, 11, 2])
sz = len(A)

Table = np.zeros((sz, sz))

T = 29

for i in range(sz): #start from left most, move to right column
	for j in range(i, -1, -1):
		#if adding same number to itself, set to column
		if j == i:
			if A[i] > T:
				Table[j, i] = 0
			else:
				Table[j, i] = A[i]
		else:
			val = 0
			for k in range(j + 1, i + 1, 1):
				# print('j:{} k:{} i:{}'.format(j, k, i))
				#find previous highest value
				if Table[k, i] > val:
					 val = Table[k, i]

			if A[j] + val <= T:
				Table[j, i] = A[j] + val
			else:
				Table[j, i] = val
print('looking for {}'.format(T))
print(A)
print(Table)