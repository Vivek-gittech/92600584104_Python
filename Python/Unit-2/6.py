lists=[10,20,30,40,50,60]
str="Hello Wolrd"
dict={
    'name':'vivek',
    'college':'Marwadi University'
}

print("Display in the lists")
for i in lists:
    print(i,end=" ")
 
print("\nDisplay in the String")
for j in str:
    print(j , end=" ")
    
print("\nDisplay in the dictionaries")
for k in dict:
    print("Dict: ",dict[k])