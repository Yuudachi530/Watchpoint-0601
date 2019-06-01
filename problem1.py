month = 1
balance = float(input("please enter your balance: "))
air = float(input("please enter your annual interest rate: "))
mpr = float(input("please enter your mounthly minimum payment rate: "))
mir = air / 12
pr = balance
while month != 13:
    mmp = mpr * pr
    mub = pr - mmp
    pr = mub + mir * mub
    month = month + 1
    
print("the remining balance is: ",pr)
    
    
    
    



