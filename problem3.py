balance = eval("please enter your balance: ")
air = eval(input("please enter your annual interest rate: "))

mir = air / 12.0
mplb = balance / 12
mpub = (balance * (1 + mir)**12) / 12.0

print((mplb + mpub)/2)

