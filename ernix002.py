def solve(s, t):
   i = j = 0
   result = ""
   while i < len(s) and j < len(t):
      result += s[i] + t[j]
      i+=1
      j+=1
   while i < len(s):
      result += s[i]
      i += 1
   while j < len(t):
      result += t[j]
      j += 1
   return result


S1 = "abc"
S2 = "def"
print(solve(S1, S2))
S1 = "David"
S2 = "Gal"
print(solve(S1, S2))