def head(list):

	return list[0]

print(head([1,2,3]))

def last(list):

	return list[len(list)-1]

print(last([1,2,3]))

def tail(list):

	list.pop(0)

	return list

print(tail([1,2,3]))

def equal_lists(list1, list2):

    len1 = len(list1)
    len2 = len(list2)

    if len1 - len2 == 0:

        lenght = 0

    start = 0
    equal = 0

    for item in list1:
        
        if item - list2[start] == 0:

            equal += 0
            
        else: equal += 1

        start += 1

    if lenght - equal == 0:

        return True

    else: return False

print(equal_lists(([1,2,3]), ([1,2,3])))



def count_item(number, list):

	count = 0

	for item in list:

		if number == item:

			count += 1

	return count

print(count_item(2,([1,2,3,2,1,4,1,4,1,1,1])))



def take(number, list):

    start = 0

    new_list = []

    while number > start:

        new_list += [list[start]]

        start += 1

    return new_list

print(take(5,([1,2,3,2,1,4,1,4,1,1,1])))


def drop(number, list):

    start = number

    new_lenght = len(list) - start

    new_list = []

    while new_lenght > len(new_list):

        new_list += [list[start]]

        start += 1

    return new_list

print(drop(5,([1,2,3,2,1,4,1,4,1,1,1])))



def reverse(list):

    start = len(list) - 1

    new_list = []

    while start > -1:

        new_list += [list[start]]

        start -= 1

    return new_list

print(reverse([1,2,3,2,1,4,1,4,1,1,1]))
