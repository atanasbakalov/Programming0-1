n = int(input("Type a number:" + "\n"))

start = 2

is_prime = True

if n == 1:
   
   is_prime = False
   
while start < n:

   if n % start == 0:
      
      is_prime = False
   
      break

   start = start + 1
   
if is_prime:
      
   print("Number is prime")
      
else:
      
   print("Number is not prime")

