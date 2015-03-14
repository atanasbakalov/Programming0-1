x = int(input("Type a number" + "\n"))

lst = [int(i) for i in str(x)]

print(lst)

print(int("".join(str(z) for z in lst)))
