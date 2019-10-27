import pandas as pd
import numpy as np 

def Get_B_Coefficients(y,x):
    xt = np.transpose(x)
    inv = np.linalg.inv(np.matmul(xt,x))
    return np.matmul(np.matmul(inv,xt),y)

df = pd.read_csv("test.csv")
x_df = df[['Health_Expenditure','GDP_Per_Capita','Primary_School_Enrollment','Secondary_School_Enrollment','Tertiary_School_Enrollment','Unemployment']]
y_df = df[['Life_Expectancy']]

x = x_df.to_numpy()
y = y_df.to_numpy()

b = OLS.Get_B_Coefficients(y,x)