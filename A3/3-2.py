import numpy as np

string1 = "fire"
string2 = "icef"

#add space for table padding
string1 = " " + string1
string2 = " " + string2

sz1 = len(string1)
sz2 = len(string2)

dimensions = (sz1, sz2)

Table = np.zeros(dimensions)
out = ""
temp = 0

for i in range(1, sz1):	#row
	for j in range(1, sz2):	#col
		val = 0
		
		#if match
		top = Table[i - 1, j]
		top_left = Table[i - 1, j - 1]
		left = Table[i, j -1]

		if(string1[i] == string2[j]):
			if(top == top_left):
				val = top + 1
			elif top > left:
				val = top
			else:
				val = left
		else:
			if left > top:
				val = left
			else:
				val = top

		Table[i, j] = val
			#increment iff top left == top
			#else current = top
		# else current == greater of top or left cell
		
# print('Insertions till equal: {}'.format())
# print('Deletions till equal: {}'.format())
# print('Replacements till equal: {}'.format())

val = Table[sz1 - 1, sz2 - 1]
sz1 =  sz1 - val - 1
sz2 = sz2 - val - 1

if sz1 > sz2:
	diff = sz1
else:
	diff = sz2

print('operations to make them equal: {}'.format(diff))
print(out)
print(string1[1:])
print(string2[1:])