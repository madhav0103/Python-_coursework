# operations of strings
n1="vikash"
n2="yadav"
print("concatenation of strings:",n1+n2)
print("vikash" *3)
print(n1[4])
print(n2[2])
print(n1[0:4])
print(n2[:2])
print('vikash' in n1)
print("python" not in n2)

#built in string functions
k="python programming"
print(len(k))
print(max('Vikash'))
print(min("Vikash"))
print(sorted('python'))
print(chr(97))
print(ord('s'))

#python string methods 
# case conversion methods
x="health is wealtth"
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.title())
y='PyThOn'
print(y.swapcase())


# Alignment and formatting methods
y='tit for tat'
print(y.center(30,"*"))
print(y.center(20,"_"))
print(y.rjust(20,'_'))
print(y.ljust(20,"_"))
w="899"
print(w.zfill(5))


#search and find methods
u="varunsanjaytharun"
print(u.find("sanjay"))
print(u.find('s'))
print(u.count('a'))
print(u.index('v'))
print(u.rfind("a"))