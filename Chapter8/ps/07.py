l=["priyanshu","ashok","harry","am"]

def rem(l,word):
	n=[]
	for item in l :
		if not(item == word):
			n.append(item.strip(word))
	return n
word=inpurt('Enter your remove name :')
print(rem(l,word))
