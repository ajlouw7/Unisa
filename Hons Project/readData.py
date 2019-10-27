import pandas as pd
import numpy as np 
import math
import kNN as KNN
import OLS as OLS



df = pd.read_csv("test.csv")

#rrs = KNN.getKNN(df, df.head(1),3)
#av = KNN.avgOfKNN(df,df.head(1),3)
x_df = df[['Health_Expenditure','GDP_Per_Capita','Primary_School_Enrollment','Secondary_School_Enrollment','Tertiary_School_Enrollment','Unemployment']]
y_df = df[['Life_Expectancy']]

x = x_df.to_numpy()
y = y_df.to_numpy()




b = OLS.Get_B_Coefficients(y,x)




#x_inverse = np.linalg.inv(x)

for a in b:
    print(a)



#https://towardsdatascience.com/multiple-linear-regression-from-scratch-in-numpy-36a3e8ac8014

i = 0




 #   data.