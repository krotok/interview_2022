#Recursion and Nested Lists
#A nested list can be traversed and flattened using a recursive function. The base case evaluates an element in the list. If it is not another list, the single element is appended to a flat list. The recursive step calls the recursive function with the nested list element as input.

def flatten(mylist):
    flatlist = []
    for element in mylist:
        if type(element) == list:
            flatlist += flatten(element)
        else:
            flatlist += element
    return flatlist


print(flatten(['a', ['b', ['c', ['d']], 'e'], 'f']))
lst = ['1','2','3']
lst.append(lst)
print(flatten(lst))
# returns ['a', 'b', 'c', 'd', 'e', 'f']