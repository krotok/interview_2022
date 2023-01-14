#Recursive
def is_palindrome(str):
  if len(str) < 2:
    return True
  if str[0] != str[-1]:
    return False
  return is_palindrome(str[1:-1])

my_string = "qqqwww"
print("Is", "\b" if is_palindrome(my_string) else "not", "palindrome" )