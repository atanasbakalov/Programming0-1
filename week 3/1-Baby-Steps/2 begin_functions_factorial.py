def factorial(n):
    
    if n == 0:
        
        return 1
    
    else:
        
        return n * factorial(n-1)

n = int(input("Type a number:" + "\n"))

print("Factorial of your number is:", factorial(n))
