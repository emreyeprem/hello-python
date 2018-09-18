total_amount = int(input("Enter total amount: "))
tip_percentage = int(input("Enter tip % amount: "))

def tipcalc():
    print(total_amount * (tip_percentage / 100))
tipcalc()
    
