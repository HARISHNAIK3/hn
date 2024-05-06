import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
f=6
x=np.sin(2*np.pi*f*t)
with open('binary.txt',"wb") as R:
	R.write(x)
print("File has been read and write successfully")
