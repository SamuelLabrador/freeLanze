#Samuel Labrador
#slabr003@ucr.edu
import numpy as np

string1 = "Samuel"
string2 = "Breakfest"

#add space for table padding
string1 = " " + string1
string2 = " " + string2

#get the size of the strings
sz1 = len(string1)
sz2 = len(string2)


dimensions = (sz1, sz2)

#initialize the LUT
Table = np.zeros(dimensions)

for i in range(1, sz1):	#row
	for j in range(1, sz2):	#col
		val = 0
		
		#set up the variables for their corresponding data cells
		top = Table[i - 1, j]
		top_left = Table[i - 1, j - 1]
		left = Table[i, j -1]

		#see if the characters are equal
		if(string1[i] == string2[j]):
			if(top == top_left):
				val = top + 1
			elif top > left:
				val = top
			else:
				val = left

		#take the greater of the value to the left or the top
		else:
			if left > top:
				val = left
			else:
				val = top

		Table[i, j] = val
			
#To make A == B, take the longest common substring out of B.
#The remaining character count in B represents how many character of 
#A need to be changed			
val = Table[sz1 - 1, sz2 - 1]

#output
print('operations to make A equal to B: {}'.format(sz2 - val - 1))
print('A = {}'.format(string1[1:]))
print('B = {}'.format(string2[1:]))

