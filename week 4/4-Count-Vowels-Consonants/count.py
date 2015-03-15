def count_vowels_consonants(string):

    result = {
            "vowels": 0,
            "consonants": 0,
            }
    
    for char in string:
        
        if char in vow:
            
            result['vowels'] += 1
            
        elif char in cons:
            
            result['consonants'] += 1
            
    return result

vow = "aeiouyAEIOUY"
cons = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

print(count_vowels_consonants("aaaAcccD"))
