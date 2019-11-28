import pandas as pd
import numpy as np 
import Utils as utils
import kNN as knn
import kfold as kfold
import OLS as ols

class CentroidData:
    def __init__(self):
        self.centoid = []
        self.nearestDataPoints = []
        #for performance
        self.nearestDataPointsTempList = []
        #testing data for centroid
        self.testingData = []
        #for performance
        self.nearestDataPointsTempListForTestingData = []

class CentroidResults:
    def __init__(self):
        self.centroidData = []
        self.olsRuns = []

def randomN(df):
    return pd.DataFrame( np.random.rand(1,11), columns=df.columns)

def getKCentroids(k,df):
    list = []
    for i in range(k):
        list.append( randomN(df) )
    return list
    

#sort datapoints according to nearest centroid


def getInitialCentroidDatas(k,df):    
    centroidDatas = []
    centroids = getKCentroids(k,df)
    for i in range(len(centroids)):
        centroidData = CentroidData()
        centroidData.centoid = centroids[i]
        centroidData.centoid.Country_Name = 'Centroid' + str(i)
        centroidData.nearestDataPoints = pd.DataFrame( columns=df.columns)
        centroidDatas.append(centroidData)
    return centroidDatas

def getClosestCentroid(datapoint,centroidDatas):
    closestCentroidData = []
    closestDistance = 9999999999.9
    for i in range(len(centroidDatas)):
        #distance = knn.distance(centroidDatas[i].centoid, datapoint)
        distance = utils.GetEuclideanDistanceBetweenFeatureVectors(kfold.getX(centroidDatas[i].centoid),kfold.getX(datapoint) )


        if( distance < closestDistance):
            closestCentroidData = centroidDatas[i]
            closestDistance = distance
    return closestCentroidData


#closest = getClosestCentroid(df.head(1),centroidDatas )


def getMeanPoint(nearestDataPoints,trainingData):
    meanPoint = randomN(trainingData)

    meanPoint.head(1).Health_Expenditure = nearestDataPoints['Health_Expenditure'].mean()
    meanPoint.head(1).GDP_Per_Capita = nearestDataPoints['GDP_Per_Capita'].mean()
    meanPoint.head(1).Unemployment = nearestDataPoints['Unemployment'].mean()
    meanPoint.head(1).Education = nearestDataPoints['Education'].mean()
    return meanPoint





def CalculateCentroids(trainingData, k, movingThreshold, centroidDatas):
    for j in range(100):
        #assign training data point to closest centroid
        for i in range(len(trainingData)):
            dataRow = trainingData.iloc[i]
            centroidData = getClosestCentroid( dataRow, centroidDatas)
            centroidData.nearestDataPointsTempList.append(dataRow)
            #centroidData.nearestDataPoints = centroidData.nearestDataPoints.append( dataRow, ignore_index=True,sort=False )

        numberOfCentroidsThatDidNotMove = 0
        for i in range(len(centroidDatas)):
              #removing all nearest points
            centroidDatas[i].nearestDataPoints.dropna()
            centroidDatas[i].nearestDataPoints = pd.DataFrame(centroidDatas[i].nearestDataPointsTempList, columns=trainingData.columns)
            # centroidDatas[i].nearestDataPoints = pd.concat( [centroidDatas[i].nearestDataPoints, centroidDatas[i].nearestDataPointsTempList])
            #clear temp list 
            centroidDatas[i].nearestDataPointsTempList = []
            newCentroid = getMeanPoint(centroidDatas[i].nearestDataPoints,trainingData)
           
        
        
        
            #calculate mean of data points assigned to the centroid
            #newCentroid = utils.GetMeanPointOfDataset( centroidDatas[i].nearestDataPoints)
            #get the change in position of the centroid
            old = kfold.getX(centroidDatas[i].centoid)
            new = kfold.getX(newCentroid)
            diffrenceInCentroid = old - new 
            distanceBetweenOldAndNewCentroid = utils.GetEuclideanDistanceBetweenFeatureVectors(kfold.getX(centroidDatas[i].centoid),kfold.getX(newCentroid) )
            print( "centroid difference " + str(i) + ' distance= ' + str(distanceBetweenOldAndNewCentroid) )
            print( diffrenceInCentroid )
            #set new mean of data points as the new centroid
            centroidDatas[i].centoid = newCentroid
            if( distanceBetweenOldAndNewCentroid < movingThreshold ):
               numberOfCentroidsThatDidNotMove = numberOfCentroidsThatDidNotMove +1

        #return if none of the centroids have moved
        if( numberOfCentroidsThatDidNotMove >= k):
            return centroidDatas
    # return if a 100 itterations have been reached
    return centroidDatas


k = 2

#cen = CalculateCentroids(kfold.testSet(1).trainingDF, k)


#trainingX = kfold.getX(ts.trainingDF).to_numpy()
#trainingY = kfold.getY(ts.trainingDF).to_numpy()
#testingX = kfold.getX(ts.testingDF).to_numpy()
#testingY = kfold.getY(ts.testingDF).to_numpy()


#results = ols.RunDataset( trainingY, trainingX, testingY, testingX)

def RunClustering(testSet, k, movingThreshold):
    centroidResults = CentroidResults()

    centroidDatas = getInitialCentroidDatas(k,testSet.trainingDF)  

    cen = CalculateCentroids(testSet.trainingDF, k, movingThreshold, centroidDatas)
    
    #associate testing data to centroids
    for i in range(len(testSet.testingDF)):
        dataRow = testSet.testingDF.iloc[i]
        centroidData = getClosestCentroid( dataRow, centroidDatas)
        centroidData.nearestDataPointsTempListForTestingData.append(dataRow)
    
    for i in range(k):
        cen[i].testingData = pd.DataFrame(centroidDatas[i].nearestDataPointsTempListForTestingData, columns=testSet.testingDF.columns)

        trainingX = kfold.getX(cen[i].nearestDataPoints).to_numpy()
        trainingY = kfold.getX(cen[i].nearestDataPoints).to_numpy()
        testingX = kfold.getX(cen[i].testingData).to_numpy()
        testingY = kfold.getY(cen[i].testingData).to_numpy()
        results = ols.RunDataset( trainingY, trainingX, testingY, testingX)
        #store centroid data in results
        centroidResults.centroidData.append(cen[i])
        #store results of running ols on the test data for that centroid
        centroidResults.olsRuns.append( results )
    return centroidResults

r = RunClustering(kfold.testSet(1), k, 0.1 )
#l = getKCentroids(2)

#a = randomN()

dist = utils.GetEuclideanDistanceBetweenFeatureVectors( a, x_df.head(1).to_numpy())






b = 1