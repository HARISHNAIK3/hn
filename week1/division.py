def check(a):
	if(a != "" and a[0] == '-'):
		return 1
	else:
		return 0	
a=input("Enter the number: ")
b=input("Enter the number: ")
acopy = a.replace(".", "")
bcopy = b.replace(".", "")
if (check(a)):
	acopy = acopy.replace("-", "")
if (check(b)):
	bcopy = bcopy.replace("-", "") 

if ((a.isnumeric() or acopy.isnumeric()) and (b.isnumeric() or bcopy.isnumeric()) ):
	print(float(a) / float(b))
else:
	print("Incorrect data")
