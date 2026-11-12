l=["priyanshu","ashok","harry","am"]

def rem(l,word):
	n=[]
	for item in l :
		if not(item == word):
			n.append(item.strip(word))
	return n
word=input('Enter remove word :')
print(rem(l,word))
print("1) priyanshu , 2) ashok")
