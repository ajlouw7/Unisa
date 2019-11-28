import math
import pandas as pd
import Utils as utils
import kfold as kfold
import OLS as ols

class Result:
    def __init__(self):
        self.distance = 0.0
        self.lifeExpectancy = 0.0
        self.country = ''
        self.year = 0

def distance(p1,p2):
    squareDistance = 0
    squareDistance += math.pow(p1.Health_Expenditure - p2.Health_Expenditure,2)
    squareDistance += math.pow(p1.GDP_Per_Capita - p2.GDP_Per_Capita,2)
    squareDistance += math.pow(p1.Education - p2.Education,2)
    squareDistance += math.pow(p1.Unemployment - p2.Unemployment,2)
    
    return math.sqrt(squareDistance)



def getKNN(df, target, k):
    results = list()
    targetCountryName = target.Country_Name
    for p2 in df.itertuples():
        #ignoring data points from the same country 
        if targetCountryName != str(p2.Country_Name): 
            r = Result()
            r.distance = distance(target,p2 )
            r.lifeExpectancy = p2.Life_Expectancy
            r.country = p2.Country_Name
            r.year = p2.Year
            results.append(r)  
    results.sort(key=lambda x:x.distance)
    return results[0:k]

def avgOfKNN(df,target,k):
    results = getKNN(df,target,k)
    sumLifeExpectancy = 0.0
    for r in results:
        sumLifeExpectancy += r.lifeExpectancy
    return sumLifeExpectancy/k

def kNNRunDataset(k,testset):
    trainingDF = testset.trainingDF
    testingDF = testset.testingDF
    run = ols.OLSRun()
    for testDataPoint in testingDF.itertuples():
        result = ols.RunResult()
        knnResults = getKNN(trainingDF, testDataPoint,k)
        #calculate averageOfPoints
        sumLifeExpectancy = 0.0
        for r in knnResults:
            sumLifeExpectancy += r.lifeExpectancy
        predictedLifeExpectancy = sumLifeExpectancy/k
        #calculate Error
        result.error = abs( predictedLifeExpectancy - testDataPoint.Life_Expectancy )
        result.lifeExpectancy = testDataPoint.Life_Expectancy
        result.predictedLifeExpectancy = predictedLifeExpectancy
        result.inputFeatureVector = testDataPoint
        run.results.append( result )
    return run



#def RunDataset(trainingLifeExpectancies,
#               trainingFeatureVectors,
#               testLifeExpectancies,
#               testFeaturevectors):
    
#df = pd.read_csv("test.csv")

#rrs = getKNN(df, df.head(1),3)
#av = avgOfKNN(df,df.head(1),3)

#x_df = df[['Health_Expenditure','GDP_Per_Capita','Primary_School_Enrollment','Secondary_School_Enrollment','Tertiary_School_Enrollment','Unemployment']]
#y_df = df[['Life_Expectancy']]

#x = x_df.to_numpy()
#y = y_df.to_numpy()