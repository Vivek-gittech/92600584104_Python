number=[1,2,3,4,5,6,7,8,9,10]

print("This is the Iterable")

for i in number:
    print(i)

print("This is the Iterator")

number_iterator=iter(number)
print(next(number_iterator))
print(next(number_iterator))