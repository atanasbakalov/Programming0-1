def reverse(string):

    new_string = ""

    start = len(string)-1

    while start > -1:

        new_string += str(string[start])

        start -= 1

    return new_string

print(reverse("Atanas"))


def reverse(string):

    result = ""

    for ch in string:

        result = ch + result

    return result

print(reverse("Atanas"))


def join(delimiter, items):

    result = ""

    last_index = len(items)-1

    index = 0

    for item in items:

        if index == last_index:

            result = result + item

        else:

            result = result + item + delimiter

        index += 1

    return result

print(join(" ", ["Radoslav", "Yordanov", "Georgiev"]))


def startswith(search, string):

	start = 0

	check = 0

	for ch in search:

		if ch == string[start]:

			check += 0

		else: check += 1

		start += 1

	if check == 0:

		return True

	else:

		return False

print(startswith("Winter", "Winter is comming"))


def endswith(search, string):
    
    new_string = ""

    start = len(search)-1

    while start > -1:

        new_string += str(search[start])

        start -= 1

    end = len(string)-1

    check = 0

    for ch in new_string:

        if ch == string[end]:

            check += 0

        else:

            check += 1

        end -= 1

    if check == 0:

        return True

    else:

        return False

print(endswith("comming", "Winter is comming"))



def trim(string):

    while string.endswith(" "):

        string = string[:-1]
        
    while string.startswith(" "):

        string = string[1:]

    return string
    
print(trim("   Game of Thrones   "))



def string_to_char_list(string):

    result = []

    for ch in string:

        result = result + [ch]

    return result


def char_list_to_string(list):

    result = ""

    for item in list:

        result = result + item

    return result

print(char_list_to_string(["A", "t", "B"]))


def change_string(index, ch, string):

    char_list = string_to_char_list(string)

    char_list[index] = ch

    return char_list_to_string(char_list)


