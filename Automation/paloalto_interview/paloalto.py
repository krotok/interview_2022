import json

dictionary = {
    "id": "04",
    "name": "sunil",
    "department": "HR"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)
print(json_object)

json_object = '{ "name":"John", "age":30, "city":"New York"}'
dict_obj = json.loads(json_object)
dict_obj["name2"] = "John222"
for i,y in dict_obj.items():
    print(f"{i}  {y}")
print(dict_obj["name"])


#######################
my_str = "the the ttt the the ttt"
my_lst = my_str.split()
print(my_str)
my_dict = {}

ttt = my_dict.keys()

for word in my_lst:
    try:
        ttt = my_dict.keys()
        print(f"Keys: {ttt}")
        if word in my_dict.keys():
            print(f"WORD: {word}")
            my_dict[word] = my_dict[word] + 1
        else:
            my_dict[word] = 1
    except():
        my_dict[word] = 1

for x, y in my_dict.items():
    print(f"key : {x} , value {y}")

# for word in my_lst:
#     print(word)
