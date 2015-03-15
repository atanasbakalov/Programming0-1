from random  import randint, shuffle

def generate_test(count):
    
    names = ["Ivo", "Maria", "Anetta", "Philip", "Rado", "Gergana"]

    result = []

    for name in names:
        
        result = result + [name] * randint(1, count)
    
    shuffle(result)

    return result


def count_visitors(checked):
    
    counted = []
    
    for person in checked:
        
        if person not in counted:
            
            counted += [person]

    return len(counted)

print("Visitors checked in:", count_visitors((generate_test(20))))
