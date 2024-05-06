import pickle
import numpy as np
from matplotlib import pyplot as plt
f=open("pickle.pkl",'wb')
pickle.dump(a,f)
pickle.dump(b,f)
pickle.dump(c,f)
f.close()
f=open("file.pkl",'r')
a=pickle.load(f)
b=pickle.load(f)
f.close()
