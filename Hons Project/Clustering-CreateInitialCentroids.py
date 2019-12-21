import pandas as pd
import numpy as np 
import Utils as utils
import kNN as knn
import kfold as kfold
import OLS as ols


exampleDF = kfold.testSet(1).testingDF

df = pd.DataFrame(columns=exampleDF.columns) 

index = 0
delta = 1


for i in np.arange(0.0,1.1,delta):
    for j in np.arange(0,1.1,delta):
        for k in np.arange(0,1.1,delta):
            for l in np.arange(0,1.1,delta):
                df.at[index,'Unnamed: 0'] =1
                df.at[index,'Country_Name'] =1
                df.at[index,'Year'] = 1
                df.at[index,'Life_Expectancy'] =1
                df.at[index,'Primary_School_Enrollment'] =1
                df.at[index,'Secondary_School_Enrollment'] =1
                df.at[index,'Tertiary_School_Enrollment'] = 1
                df.at[index,'Health_Expenditure'] = i
                df.at[index,'GDP_Per_Capita'] = j
                df.at[index,'Education'] = k
                df.at[index,'Unemployment'] = l
                index =  index + 1

df.to_csv('clustering-InitialCentroids' + str(delta) + '.csv')