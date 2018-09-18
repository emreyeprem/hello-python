number = int(input('Enter your number: '))
def troop():
     if(number % 15 == 0):
         print('fizzBuzz')
     elif(number % 3 == 0):
         print('Fizz')
     elif(number % 5 == 0):
         print('Buzz')
     else:
         print('Undefined')

troop()
