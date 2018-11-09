import numpy as np

target = 'nonutnovember'
sz = len(target)
target = " " + target + " "

Table = np.zeros((sz + 2, sz + 2))

largest = 0

for i in range(1, sz + 1): #row
	flag = 0
	for j in range(sz, i - 1, -1): #column
		

		top_right = Table[i - 1, j + 1]
		top_left = Table[i - 1, j - 1]

		if flag == 1 :
			Table[i, j] = Table[i, j + 1]
		
			#account for single element inside palindrome
			if i == j and top_right > 1 and top_left > 1 :#and target[i] != target[i + 1]:
				Table[i, j] = Table[i - 1, j] + 1

		elif target[i] == target[j]:
			if (top_right > 1 and i != j and top_left > 1):
				Table[i, j] += 2 + Table[i - 1, j]
			elif i == j:
				if top_right > 1 and top_left > 1 and target[i] != target[i + 1]:
					Table[i, j] += 1 + Table[i, j + 1]
				else:
					Table[i, j] = Table[i, j + 1]
			else:	
				Table[i, j] = 2
			flag = 1
		else:
			Table[i, j] = Table[i - 1, j]
		
		if(Table[i, j] > largest):
			largest = Table[i, j]

print(largest)
print(target[1:])
print(Table)