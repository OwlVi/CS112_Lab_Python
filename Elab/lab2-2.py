#INPUT 
import math
w = float(input("Enter width: "))
l = float(input("Enter length: "))
d = float(input("Enter depth: "))
#PROCESS
area = w*l*d
result = area*5
#OUTPUT
print("Steve will take {:d} minutes.".format(math.ceil(result/60)))