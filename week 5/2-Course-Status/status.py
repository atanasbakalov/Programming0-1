def status_count(students):

    finalized = []
    not_finalized = []

    for student in students:
        
        if(student["status"])== "finalized":
            
            finalized = finalized + [student["name"]]
            
        elif(student["status"])== "not_finalized":
            
            not_finalized = not_finalized + [student["name"]]       
            
    return {
  "finalized": finalized,
  "not_finalized": not_finalized
  }

students = [{"name": "RadoRado","status": "not_finalized"},
            {"name": "Ivo","status": "finalized"},
            {"name": "Genadi","status": "finalized"}]

print(status_count(students))
    
