#importing library for computing permutation
from itertools import permutations
i = input().split(" ") #for same line input
a = i[0]
b = int(i[1])
l=[]
t=0
ind = 0
if (1 <= int(a) <= 10000000) and (1 <= b <= 10000000):
	a1 = [''.join(p) for p in permutations(a)] #creating list of permuation possible for 'a'
	a1.pop(0) #Deleting the 1st value in list as 1st value is a duplicate value of the original number
	for i in range(len(a1)):
		a1[i] = int(a1[i])
		z = a1[i] - b #Checking the difference between 2nd number & permuted value
		l.append(z)
	min_val = 10000000
	#checking for the minimum difference that is > 0
	for i in l:
		if min_val>i and i>0:
			min_val = i
			ind = l.index(i) #Storing the index of min_val found in 'l'
	#Finding the nearest number to 'b' using the above index value
	for i in range(len(a1)):
		if i==ind:
			t=a1[i]
			break
	#Output
	if int(t)>int(b):
		print(t)
	else:
		print(str(-1))
