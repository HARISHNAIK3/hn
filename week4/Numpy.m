t=0:0.01:1;
frequency=2;
x=sin(2*pi*frequency*t);
save_binary'numpy.bin'x;
