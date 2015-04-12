def is_string_palindrom(string):

    banned = [",", ".", "!", "?"]

    string = string.replace(" ", "")

    string = string.lower()

    updated_string = ""

    for ch in string:

        if ch not in banned:

            updated_string = updated_string + ch

    new_string = ""

    for ch in string:

        if ch not in banned:

            new_string = ch + new_string
     
    if new_string == updated_string:

        return True

    else:

        return False
    
print(is_string_palindrom("Az obi4am ma4 i boza"))
print(is_string_palindrom("A Toyota!"))
print(is_string_palindrom("bozaaa"))
print(is_string_palindrom(" kapak! "))
