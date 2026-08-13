a = [10, 20, 30, 40, 50]

print("List =", a)

print("First element =", a[0])
print("Last element =", a[-1])

print("Slicing =", a[2:4])

a.append(60)
print("After append =", a)

a.remove(20)
print("After remove =", a)

b = [x * 2 for x in a]
print("List comprehension =", b)