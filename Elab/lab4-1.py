balance  = float(input("Enter Balance: "))

while (balance >= 0):
    select = input(" Deposit (1) / Withdraw (2) / Exit (3) \n: ")
    if select == '1' or select == "Deposit" or select == "deposit":
        deposit  = float(input("Enter Deposit: "))
        if deposit < 0 :
            print("Cant not deposit")
            break
        balance += deposit
    elif select == '2' or select == "Withdraw" or select == "withdraw":
        withdraw = float(input("Enter Withdraw: "))
        if withdraw < 0:
            print("Cant not withdraw")
            break
        balance -= withdraw
    else:
        break
print("My Balance: {:.2f}".format(balance))
