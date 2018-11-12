import numpy as np

target = 6
targetCount = 0

diceSize = 6
Dice = np.array(range(1, diceSize + 1))
diceCount = 3


Table = np.zeros((diceSize + 1, diceSize + 1))

for i in range(0, diceCount):
	for j in range(1, diceSize + 1):
		for k in range(1, diceSize + 1):
			targetCount = 0
	print(Table)

print(targetCount)