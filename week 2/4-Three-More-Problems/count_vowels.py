n = input("Type a text" + "\n")

counter = 0

counter = int(counter)

vowels = "aeiouyAEIOUY"

for i in n:
    
    if i in vowels:

        counter += 1
        
print("The number of vowels in your string is:", counter)
