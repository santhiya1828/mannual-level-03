print("TAKSHAHILA UNIVERSITY")
print("ONGUR TINDIVANAM")
print("----------------")
print("student make list")
pymark=int(input("enter python mark:"))
dbmsmark=int(input("enter dbms mark:"))
acmark=int(input("enter accounting mark:"))
total=pymark+dbmsmark+acmark
print("total mark:",total)
avg=total/3
print("average marek:",avg)
if pymark>=40 and dbmsmark>=40 and acmark>=40:
    print("resutl:pass")
if total>=250:
    print("grade:O grade*")
elif tolta>=200:
    print("grade:A+ grade*")
elif total>=150:
    print("grade:A grade*")
else:
    print("grade:B grade*")
    print("result:fail")
    print("grade no grade(failed")
