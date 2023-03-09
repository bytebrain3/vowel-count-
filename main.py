user = str(input("string : "))
array =[]
for c in user:
	if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
		array.append(c)
print("total vowel count ",len(array))


a = []
e =[]
i =[]
o =[]
u=[]

for q in array:
	if q == "a":
		a.append(q)
	elif q == "e":
		e.append(q)
	elif q == "i":
		i.append(q)
	elif q == "o":
		o.append(q)
	elif q == "u":
		u.append(q)
	elif q == "A":
		a.append(q)
	elif q == "E":
		e.append(q)
	elif q == "I":
		i.append(q)
	elif q == "O":
		o.append(q)
	elif q == "U":
		u.append(q)
if len(a)>0:
	print("total number of a is ",len(a))
if len(e)>0:
	print("total number of e is ",len(e))
if len(i)>0:
	print("total number of i is ",len(i))
if len(o)>0:
	print("total number of o is ",len(o))
if len(u)>0:
	print("total number of u is ",len(u))
