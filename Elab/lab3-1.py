
#input 

money = float(input("Enter buying amount: "))

#process
if money > 3000 :
      print("Amount due after discount is {:.2f} baht.".format(money-(money*0.35)))
elif money >= 1500:
      print("Amount due after discount is {:.2f} baht.".format(money-(money*0.20)))
elif money >= 750:
      print("Amount due after discount is {:.2f} baht.".format(money-(money*0.1)))
elif money > 300:
      print("Amount due after discount is {:.2f} baht.".format(money-(money*0.05)))
else:
      print("Amount due after discount is {:.2f} baht.".format(money))
