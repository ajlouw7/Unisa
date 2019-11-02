import pandas as pd
import numpy as np 

#caluclate training coefficcients array
#y - 1d array of results or dependant variable instances
#x - 2d array of feature vetors for each data point 
def Get_B_Coefficients(y,x):
    xt = np.transpose(x)
    inv = np.linalg.inv(np.matmul(xt,x))
    return np.matmul(np.matmul(inv,xt),y)

df = pd.read_csv("test.csv")
x_df = df[['Health_Expenditure','GDP_Per_Capita','Primary_School_Enrollment','Secondary_School_Enrollment','Tertiary_School_Enrollment','Unemployment']]
y_df = df[['Life_Expectancy']]

x = x_df.to_numpy()
y = y_df.to_numpy()

firstx = x_df.head(1).to_numpy() 
firsty = y_df.head(1).to_numpy()

b = Get_B_Coefficients(y,x)

print('B: ')
print(b)

print('X vector')
print(firstx)

def EvaluateModel(featureVector, B_Coefficients):
    return np.matmul(featureVector,B_Coefficients)

estimate = EvaluateModel(firstx,b)

print('Y')
print(firsty)

print('Estimate')
print(estimate)
error = estimate - firsty

print('Error')
print( error ) 

class RunResult:
    inputFeatureVector = []
    lifeExpectancy = 0.0
    predictedLifeExpectancy = 0
    error = 0

class OLSRun:
    results = []
    itemCount = 0
    averageError = 0


def RunDataset(ys,featureVectors):
    # calculate B
    b = Get_B_Coefficients(ys,featureVectors)
    run = OLSRun()
    errorSum = 0
    
    # itterate through data items to get predicted values
    for i in range(len(featureVectors)):
        item = RunResult()
        item.lifeExpectancy = ys[i]
        item.inputFeatureVector = featureVectors[i]
        item.predictedLifeExpectancy = EvaluateModel(item.inputFeatureVector,b)
        item.error = abs(item.lifeExpectancy - item.predictedLifeExpectancy)
        run.results.append( item )
        errorSum += item.error
    
    run.itemCount = len(featureVectors)
    run.averageError = errorSum/run.itemCount
    return run

r = RunDataset(y,x)
a = 0