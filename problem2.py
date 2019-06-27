mounth = 1
balance = float(input("please enter your balance: "))
air = float(input("please enter your annual interest rate: "))
mir = air / 12
mpb = balance/12
mub = mpb + mir*mpb
print(mub)

