def is_perfect(x):
   
   sum_factors = 0
   sum_factors = int(sum_factors)
   
   for i in range(1, x):
      
       if x % i == 0:
          
           sum_factors += i

   if sum_factors == x:

      return "Number is perfect"
       
   else:

      return "Number not perfect"

print(is_perfect(496))
print(is_perfect(497))
