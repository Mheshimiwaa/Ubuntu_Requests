#Create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not. In order to accomplish this, we will need the following steps:
def large_power():
    base=int(input("enter base number:"))
    exponent=int(input("enter exponent number:"))
    result=base**exponent

    if result > 5000:
        print("True")
    else:
        print("False")
        
    return result>5000
large_power()