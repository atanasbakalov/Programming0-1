n = int(input("Enter number of words:" + "\n"))

count = 1
words_list = []

print("Enter a word:" + "\n")

while count <= n:
    
    word = input("")
    words_list += [word]

    count += 1

words_list.sort()

print()

for word in words_list:

    print(word)


