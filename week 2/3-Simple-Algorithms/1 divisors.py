def print_factors(num):

   list = []
   
   for i in range(1, num):

      if num % i == 0:

         list += [i]

   return "List of divisors is", list

print(print_factors(12))
