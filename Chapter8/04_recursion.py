def rec(n):
	if(n==1 or n==0):
		return 1
	return n*rec(n-1)

n=int(input("Enter your number :"))
print("The recursion number is ", rec(n))

