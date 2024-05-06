import numpy as np
from matplotlib import pyplot as plt
x=5
t=np.arange(0,1,0.01)
f=open("/home/viswanadh/GITHUB/Week_4/txt_1.txt","w")
np.savetxt(f,x)
f.close()
f=open("/home/viswanadh/GITHUB/Week_4/txt_1.txt","r")
data=np.loadtxt
print(data)
f.close()
