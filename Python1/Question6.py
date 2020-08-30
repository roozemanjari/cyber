def palindrome(s):
  x = True
  for i in range(0,len(s)/2):
      if(s[i] != s[len(s)-i-1]):
          x = False
          break
  return x

print(palindrome("abab")) 
print(palindrome("ababa")) 
print(palindrome("aba")) 
