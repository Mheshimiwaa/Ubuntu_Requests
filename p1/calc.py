a=input("enter a")
b=input("enter b")
operand=input("enter operator")
a=int(a)
b=int(b)
if operand =="+":
    print (a)+(b)
elif operand =="-":
    print (a)-(b)
elif operand =="*":
    print (a)*(b)
elif operand =="/":
    print (a)/(b)
elif operand =="%":
    print (a)%(b)
elif operand =="**":
    print (a)**(b)
elif operand =="//":
    print (a)//(b)

else:
    print ("invalid operator")