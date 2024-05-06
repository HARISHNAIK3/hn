list1=[]
list2=[]
sum=0
n=int(input("No of orders: "))
for i in range(n):
	x=int(input("Enter number: "))
	y=int(input("Enter number: "))
	list1.append(x)
	list2.append(y)
print("V1= ",list1)
print("V2= ",list2)
for i in range(len(R1)):
	sum+=list1[i]*list2[i]
print("Dot product: ", sum)
