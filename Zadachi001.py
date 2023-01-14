#Polindrom slices

def isPalindrome(s):
    print(s)
    print(s[::-1])
    return s == s[::-1]


# Driver code
s = "malayalam123"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

##############
a = [1,2,3,4,5,6]
print( sum(a) / len(a))
######################################
p= "".join(['John','Ray'])
print(p)

#############################
# Stack() implementation

class Stack():
    def __init__(self, my_stack=[]):
        self.__stack__ = my_stack

    def pop(self):
        return self.__stack__.pop()

    def push(self, value):
        self.__stack__.append(value)

    def size(self):
        return len(self.__stack__)

    def print(self):
        print(f"Stack {self.__stack__}")

    def empty(self):
        if (len(self.__stack__)) == 0:
            return 1

    def top(self):
        return self.__stack__[-1]


string_tmp = "[[{{}}]]"

# my_list=Stack(list(string_tmp))
# my_list.print()

my_list2 = Stack(list())
for i in string_tmp:
    if my_list2.empty():
        my_list2.push(i)
    elif i == "]":
        if my_list2.top() == "[":
            print(f"Remove element: {my_list2.pop()}")
    elif i == "}":
        if my_list2.top() == "{":
            print(f"Remove element: {my_list2.pop()}")
    else:
        my_list2.push(i)
    my_list2.print()

tmp = "a12345"
tmp = list(tmp)
a = tmp.pop()
print(f"{a}  {tmp}")