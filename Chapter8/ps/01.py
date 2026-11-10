a=int(input("Enter your number 1 :"))
b=int(input("Enter your number 1 :"))
c=int(input("Enter your number 1 :"))

def greater(a,b,c):
	if(a>b and a>c):
		return a
	elif(b>a and b>c):
                return b
	else:
		return c

print("The greater number is " , greater(a,b,c))

