n=int(input("Enter your number :"))

for i in range(2,n):
	if(n%i) == 0:
		print("This number is not a prime number")
		break
else:
	print("This number is  a prime number")


print("hello")