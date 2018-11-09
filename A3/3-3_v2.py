import numpy as np

A = np.array([4, 5, 17, 23, 11, 2])
sz = len(A)

Table = np.zeros((sz, sz))

T = 44

for i in range(sz): #start from left most, move to right column
	for j in range(i, -1, -1): #move through rows
		if j == i:
			if A[i] > T:
				Table[j, i] = 0
			else:
				Table[j, i] = A[i]
		else:
			val = 0
			for k in range(j + 1, i + 1, 1):
				if Table[k, i] + A[j] <= T and Table[k, i] + A[j] > val:
					val = Table[k, i] + A[j]

			Table[j, i] = val


print('looking for {}'.format(T))
print(A)
print(Table) 