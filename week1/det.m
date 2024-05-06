matrix=[1 2 3;4 5 6;7 8 9]
if size(martix,1)==2
det=matrix(1,1)*matrix(2,2)-matrix(1,2)*matrix(2,1);
else
det=0;
for col=1:size(matrix,2)
submatrix=matrix(2:end,[1:col-1,col+1:end);
det+=matrix(1,col*det_recursive(submatrix)*(-1)^n,col-1)
end
end
disp("determinenet",det)
