balance  = float(input("Enter Balance: "))
deposit  = float(input("Enter Deposit: "))
withdraw = float(input("Enter Withdraw: "))

print("{:^55s}".format("-----------------------My Bank-----------------------"))
print("{:^10s}|{:^14s}|{:^13s}|{:^13s}|".format("Date","WITHDRAW","DEPOSIT","BALANCE"))

balance += deposit
print("{:^10s}|{:-14.2f}|{:+13.2f}|{:-13.2f}|".format("15/03/23",0*(-1),deposit,balance))

balance -= withdraw
print("{:^10s}|{:-14.2f}|{:+13.2f}|{:-13.2f}|".format("",withdraw*(-1),0*(-1),balance))
