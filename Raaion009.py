import re

my_str = "aaabbbbccccc"
known_chars = []
my_list = list(my_str)
result = ""
print(my_list)
print(len(re.findall("a", my_str)))
# for char in my_list:
#     if char not in known_chars:
#         known_chars.append(char)
#         result = result + char + my_list.count(char)

print(result)
#new_list = list(filter(lambda x: (x%2 == 0), my_list))

my_dict = {i : my_list.count(i) for i in my_list}
my123 = ""
for i in my_dict:
    my123 = my123 + str(i) + str(my_dict[i])
print(my123)

my_dic2 ={i : my_str.count(i) for i in my_str}
print(my_dic2)