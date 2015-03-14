def sum_factors(x):
   
   sum_factors = 0
   
   for i in range(1, x):
      
       if x % i == 0:
          
           sum_factors += i

   return print("The sum of all wanted factors, without the number is:",
                sum_factors)

print(sum_factors(12))
