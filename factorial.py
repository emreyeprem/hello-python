#number = int(input("Enter Your Number: "))
#def factorial():
#    if(number == 0):
#        print(1)
#    elif(number == 1):
#        print(1)
#    elif(number < 0):
#        print("factorial does not exist for negative numbers")
#    else:
#        print(number * factorial(number - 1))

#factorial()

#second trial
#number = int(input("Enter Your Number: "))

#result = 1

#for i in range(1, number + 1, 1):
#    result = result * i
#    if(number < 0):
#        print("Sorry, factorial does not exist for negative numbers")
#    elif(number == 0):
#        print("The factorial of 0 is 1")
#    else:
#        print(result)



#third trial
#n = int(input("Enter Your Number: "))
#def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n-1)
#    print(factorial)
#factorial(n)

#fourth trial
number = int(input("Enter Your Number: "))
def factorial():
    result = 1
    for i in range(1,number + 1, 1):
        result = result * i

        if(number == 0):
            print(1)

    print(result)

def neg_factorial():
    if(number < 0):
        print("Negative numbers don't have a factorial")
    else:
        return factorial()
neg_factorial()
