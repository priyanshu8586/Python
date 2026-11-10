marke1 = int(input("Enter your marke 1:"))
marke2 = int(input("Enter your marke 2:"))
marke3 = int(input("Enter your marke 3:"))

total_persantage = (100*(marke1+marke2+marke3)/300)

if(total_persantage>=40 and marke1>=33 and marke2>=33 and marke3>=33):
    print("your are passed" , total_persantage,"%")

else:
    print("you are failed " , total_persantage,"%")