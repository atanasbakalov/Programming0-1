def calculate_coins(bill):
    
    result = {}
    
    coins = [1, 2, 100, 5, 10, 50, 20]

    coins = sorted(coins, reverse = True)

    bill = round(bill * 100)

    for coin in coins:
        
        times_to_use = bill // coin
        
        result[coin] = times_to_use

        
        bill -= times_to_use * coin
        
    return result

print(calculate_coins(8.94))
print(calculate_coins(0.53))
