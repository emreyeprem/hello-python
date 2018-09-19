string = input("Enter Your Word: ")
reverse = string[::-1]
print(reverse)
def is_palindrome():
     if(string == reverse):
         print("Yes")
     else:
         print("No")
is_palindrome()           

#def is_Palindrome(a):
#    rev = reverse(a)
#    if(a == rev):
#        return True
#    return False
