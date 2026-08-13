a = 10
b = 5

print("Arithmetic Operations:")
print(f"Addition {a} + {b} = {a+b}")
print(f"Subtraction {a} - {b} = {a-b}")
print(f"Multiplication {a} * {b} = {a*b}")
print(f"Division {a} / {b} = {a/b}")
print(f"Modulus {a} % {b} = {a%b}")

print("Relational Operations:")
print(f"{a} > {b} = {a > b}")
print(f"{a} < {b} = {a < b}")
print(f"{a} == {b} = {a == b}")
print(f"{a} != {b} = {a != b}")

print("Logical Operations:")
print(f"{a} > 5 {b} <10 = {a > 5 and b < 10}")
print(f"{a} > 15 {b} <10 = {a > 15 or b < 10}")
print(f"Not {a} > {b} = {not(a > b)}")