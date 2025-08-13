print("Government of Tamilnadu")
print("Electricity Bill")
print("-----------------")
print("Bill Receipt")
print("----------")
eb=int(input("Enter the EB.NO:"))
name=(input("Enter The Customer Name:"))
pre=int(input("Enter The Previous unit:"))
cur=int(input("Enter The Current unit:"))
Unit=cur-pre
print("Unit Consumed:",Unit)
if(Unit>=1000):
    amt=Unit*10
    print("Amount to be Paid",amt)
elif(Unit>=500):
    amt=Unit*5
    print("Amount to be Paid",amt)
elif(Unit>=100):
    amt=Unit*2
    print("Amount to be Paid",amt)
else:
    print("Amount to be Paid",Nil)
        
