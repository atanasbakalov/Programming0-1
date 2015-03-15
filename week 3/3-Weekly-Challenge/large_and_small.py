n = int(input("Enter a number:" + "\n"))

count = 1
words_list = []

ascending = ("".join(sorted(str(n))))
descending = ("".join(sorted(str(n), reverse=True)))

print("Най-голямото число с тези цифри е:", ascending)
print("Най-малкото число с тези цифри е:",descending)


