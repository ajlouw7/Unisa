import numpy as np 

def Get_B_Coefficients(y,x):
    xt = np.transpose(x)
    inv = np.linalg.inv(np.matmul(xt,x))
    return np.matmul(np.matmul(inv,xt),y)