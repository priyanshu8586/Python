n=int(input("Enter your numbr : "))
def patten(n):
	if(n==0):
		return
	print("*" * n)
	print("" * n-1)
print(patten(n))
