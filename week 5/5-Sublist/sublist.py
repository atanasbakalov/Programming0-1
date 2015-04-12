def tail(items):
    
    result = []

    for index in range(1, len(items)):        
        item = items[index]        
        result += [item]

    return result


def take(n, items):
    
    result = []
    for index in range(0, min(n, len(items))):        
        result += [items[index]]

    return result


def sublist(list1, list2):
    
  n = len(list1)

  while len(list2) != 0:      
    if take(n, list2) == list1:
        
      return True
    
    list2 = tail(list2)

  return False

print(sublist([1, 2, 3], [0, 0, 1, 2, 3, 5, 6]))
