def grades_that_pass(students, grades, limit):
    
    result = []
    
    index = 0

    for grade in grades:
        
        if grade >= limit:
            
            name = students[index]
            result = result + [name]

        index += 1  

    return result


students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]

result = grades_that_pass(students, grades, 4.0)

print(result)
    

