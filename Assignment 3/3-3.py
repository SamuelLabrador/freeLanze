import numpy as np 


A = np.array([4, 5, 17, 23, 11, 2])
A_inv = np.flip(A, 0)

sz = len(A)
table = np.zeros((sz, sz))

target = 35
# target = int(input("Enter a sum\n")) 

for i in range(sz): #iterate through columns
	#create a temp array to hold the values of the previous entries
	temp = np.zeros(i)
	for j in range(i, -1, -1): #iterate through rows based on column position

		#make s higher for loop
		s = target + 1


		if A[i] == A[j]:
			if j == sz - 1:
				table[j, i] = 0
			else:				
				table[j, i] = table[j - 1, i]
				continue

		if j == 0: #if j = 0 value should just be row + col
			s = A[i] + A_inv[j] 
			if s > target: #if sum > target set row value as target
				s = A[i]
			table[j, i] = s

		else:
			k = j
			while s > target:
				k -= 1
				s = A_inv[j] + table[k, i]
				if k < 0:
					s = A[i] + A_inv[j]
					if s > target:
						s = A[i]
					break
			if(s == target):
				table[j, i] = s
				print('true')
				print(table)
				exit()
			table[j, i] = s
print(A)
print('false')
print(table)
