#def check():
#    number = int(input("Enter a Number: "))
#    is_Prime()

#def is_Prime(a):
#    result = True
#    for i in range(2, a):
#            while result:
#               if(a%i == 0):
#                   result = False
#               else:
#                   result = True

#check()

#second trial



#def isprime(n):
    #"""Returns True if n is prime."""
#    if n == 2:
#        return True
#    elif n == 3:
#        return True
#    elif n % 2 == 0:
#        return False
#    elif n % 3 == 0:
#        return False

#    i = 5
#    w = 2

#    while i * i <= n:
#        if(n % i == 0):
#            return False

#        i += w
#        w = 6 - w

#    return True
#isprime(number)

#third trial
number = int(input("Enter a number: "))
def isPrime(n):
    if n < 2:
        return False

    for i in range(2, n, 1):
        if n % i == 0:
            return False

    return True

print(isPrime(number))                
