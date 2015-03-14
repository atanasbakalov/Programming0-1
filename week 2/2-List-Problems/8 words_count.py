x = str(input("Enter a word:" + "\n"))
n = int(input("Enter number of words:" + "\n"))

count = 1
words_list = []



while count <= n:
    
    word = input("Enter a word:" + "\n")
    words_list += [word]
    count += 1

print(x, "is found",words_list.count(x), "times.")


