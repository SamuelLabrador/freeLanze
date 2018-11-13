import numpy as np

#sum we are trying to find
target = 6

#dice parameters
diceSize = 6
#number of dice being rolled
diceCount = 6

#initialize the table
Table = np.zeros((diceCount + 1, target + 1))

#fill the first row with one
i = 1
while i <= target and i <= diceSize:
	Table[1][i] = 1
	i += 1


for i in range(2, diceCount + 1): #iterate through each of the dice
	for j in range(target + 1): #iterate though the rows
		for k in range(1, j): #iterate though the columns

			#if the col > dice, exit. we dont need to go any further
			if k > diceSize:
				break

			#add the previous row and column
			Table[i][j] += Table[i - 1][j - k]

print(Table)
#solution in the bottom right
print(Table[diceCount][target])
