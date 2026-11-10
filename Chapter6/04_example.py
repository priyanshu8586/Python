age=int(input("Eenter your age :"))
citizen = True

if(age>=18):
    if(citizen):
        print("eliglible")
    else:
        print("not eliglible")
else:
    print("underage")