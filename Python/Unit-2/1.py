no1=int(input("Enter The 1 Number: "))
no2=int(input("Enter The 2 Number: "))
no3=int(input("Enter The 3 Number: "))

if no1==no2:
    print("Equal Numbers")

if no1>no2:
    print("Number 1 is Bigger then Number 2")
else:
    print("Number 2 is Bigger then Number 1")
    
if no1 > no2 and no1 > no3:
    print("Max is the 1 Number ",no1)
elif no2 > no1 and no2 > no3:
    print("Max is the 2 Number ",no2)
else :
    print("Max is the 3 number ",no3)