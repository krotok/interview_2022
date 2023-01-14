s = 'spameggs'
print(s[1:6])
print(s[3:5])
print(s[0:-2])
print(s[3:5:-1])

# 33. Строки
s = "0123456789"
print(s.find("45"))
print(s.find("42"))

###################
str1 = "12qwersdfs"
str2 = "12qwersdfs9"
print(str1 == str2)

int1 = 123
int2 = 123
print(int1 == int2)

###################
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 5]
lst1.append(lst2)
lst1 = lst1 + lst2
print(lst1)
print(lst1.count(1))
print(sum(lst2))


# 35 Functions
def chain_sum(number):
    result = number

    def wrapper(number2=None):
        nonlocal result
        if number2 is None:
            return result
        result += number2
        return wrapper

    return wrapper


print("Results Functions")
print(chain_sum(5)())
print(chain_sum(5)(2)())
print(chain_sum(5)(100)(-10)())



