

def is_anagram(s1, s2):
    tmp1 = [x for x in s1]
    tmp2 = [x for x in s2]
    tmp1.sort()
    tmp2.sort()
    print(tmp1)
    print(tmp2)
    if tmp1 == tmp2:
        return True
    else:
        return False

def print_anagram_result(s1, s2):
    print("Current strings is ", "\b" if is_anagram(s1, s2) else "not", " anagram")

s1 = "earnix"
s2 = "xinear"
print_anagram_result(s1, s2)

s1 = "book"
s2 = "bool"
print_anagram_result(s1, s2)

s1 = "dsadmVmslkw3DD"
s2 = "mDksmw3DldaVds"
print_anagram_result(s1, s2)