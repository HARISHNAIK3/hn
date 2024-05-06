clc;
clear all;
close all;
x=[]
x1=input("Enter length of array:")
y=0
for i=1:x1
	f=input("Enter x[n]:")
end
y1=input("Enter length of y[k]:")
k=1:0.01:y1
for(i=1:x1)
	y+=x(i)*cos(2*pi*i*k
end
plot(y)
