import pandas as pd
import numpy as np 
import Utils as utils

#caluclate training coefficcients array
#y - 1d array of results or dependant variable instances
#x - 2d array of feature vetors for each data point 
def Get_B_Coefficients(y,x):
    xt = np.transpose(x)
    inv = np.linalg.inv(np.matmul(xt,x))
    return np.matmul(np.matmul(inv,xt),y)

#df = pd.read_csv("test.csv")
#x_df = df[['Health_Expenditure','GDP_Per_Capita','Education','Unemployment']]
#y_df = df[['Life_Expectancy']]

#x = x_df.to_numpy()
#y = y_df.to_numpy()

#trainingX = x_df.head(400).to_numpy()
#trainingY = y_df.head(400).to_numpy()

#testX = x_df.tail(400).to_numpy()
#testY = y_df.head(400).to_numpy()

#firstx = x_df.head(1).to_numpy() 
#firsty = y_df.head(1).to_numpy()

#b = Get_B_Coefficients(y,x)

#print('B: ')
#print(b)

#print('X vector')
#print(firstx)

def EvaluateModel(featureVector, B_Coefficients):
    return np.matmul(featureVector,B_Coefficients)

#estimate = EvaluateModel(firstx,b)

#print('Y')
#print(firsty)

#print('Estimate')
#print(estimate)
#error = estimate - firsty

#print('Error')
#print( error ) 

class RunResult:
    inputFeatureVector = []
    lifeExpectancy = 0.0
    predictedLifeExpectancy = 0
    error = 0

class OLSRun:
    results = []
    itemCount = 0
    averageError = 0

def RunDataset(trainingLifeExpectancies,
               trainingFeatureVectors,
               testLifeExpectancies,
               testFeaturevectors):
    # calculate B
    b = Get_B_Coefficients(trainingLifeExpectancies,trainingFeatureVectors)
    run = OLSRun()
    errorSum = 0
    
    noOfItemsToTest = len(testFeaturevectors)
    # itterate through data items to get predicted values
    for i in range(noOfItemsToTest):
        item = RunResult()
        item.lifeExpectancy = testLifeExpectancies[i]
        item.inputFeatureVector = testFeaturevectors[i]
        item.predictedLifeExpectancy = EvaluateModel(item.inputFeatureVector,b)
        item.error = abs(item.lifeExpectancy - item.predictedLifeExpectancy)
        run.results.append( item )
        errorSum += item.error
    
    #calculate statistics
    run.itemCount = noOfItemsToTest
    run.averageError = errorSum/run.itemCount
    return run

#r = RunDataset(trainingY,trainingX,testY,testX)

#mean = utils.GetMeanPointOfDataset(testX)

#absoluteMeanDeviation = utils.GetMeanAbsoluteDeviationOfFeatureSet(testX)
#a = 0