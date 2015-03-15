name = input("Първо име на човек"+"\n")
name2 = input("Второ име на човек"+"\n")
name3 = input("Трето име на човек"+"\n")
birthdate = int(input("Година на раждане"+"\n"))

from datetime import date
current_year = int(date.today().year)

age = current_year - birthdate

person = {"first_name": name,
          "second_name": name2,
          "third_name": name3,
          "current_age": age}

print(person)


