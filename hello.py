#first_number = input("Enter first number: ")
#second_number = input("Enter second name: ")

#first_number_as_int = int("45")
#second_number_as_int = int("70")
#some_result = first_number_as_int + second_number_as_int
#print(some_result)

#a = 10 #integer
#b = "hello" #string
#c = 10.45 #float
#d = True #boolean

#convert the input from string to int
#first_number = int(input("Enter first number: "))
#second_number = int(input("Enter second name: "))
#result = first_number + second_number

#assignment activity
#first_number = int(input("Enter first number: "))
#second_number = int(input("Enter second number: "))
#third_number = int(input("Enter third number: "))
#result2 = first_number + second_number + third_number
#print(result2)

# string concatenation

#first_name = input("Enter First Name: ")
#last_name = input("Enter Last Name: ")
#city = input("Enter City: ")
#state = input("Enter State: ")
#zip_code = input("Enter Zip Code: ")

#My name is first_name, last_name and I live in city, state zip_code
#message = "My name is " + first_name + ", " + last_name  + " and I live in " + " + city + ", " + state " " + zip_code

#message = "My name is {0}, {1} and I live in {2}, {3} {4}".format(first_name, last_name, city, state, zip_code)
#print(message)



#message = "Hello " + "World" + "And" + "This" + "Year"
#print(message)

# functions or methods
#send_email()

#python (function define)


#def add (first_number,second_number):
#    return first_number + second_number
#    result = add(2,3)
#    print(result)





#def greet(name,age):
#    print("Hello ," + name)

#    greet("John",32)

    #this is not the correct order to pass the arguments
    #greet(32,"John")



#def greet():
#     print("I am inside the greet function")

 #  def greetJohn():
#     print("Hello John!")

#    inside the functions

#outside the function
#print("I am outside the greet function")

def display_car_information(make,model):

    print("Make {0} - Model {1}".format(make,model))

    dispaly_car_information("Honda", "Accord")

    #explicitly specify the name of the parameters(it works)
    dispaly_car_information(model = "Accord", make = "Honda")


    #  ---- CONDITIONS

    if (1==1):
        print("EQUAL")
       a = 10
       b = 10
       c = a + b

    #else:
    #    print("NOT EQUAL")


    #def evenOrOdd(number):
    #    if(number % 2 ==0):
    #        print("EVEN")
    #    else:
    #        print("ODD")
  #evenOrOdd(7)


   #age = 20
   #input =("Enter Age: ")
  #def validate_age(age):
    #  age = 10
     # if(age >= 18):
    #      print("age is greater than or equal to 18")
    #elif(age < 13):
    #    print("age is less than 13")

    #else:
    #    print("age is not greater than 18 and not less than 13")

    #    validate_age(age) #we are passing 20
    #    print("The value of age is{0} ".format(age))
