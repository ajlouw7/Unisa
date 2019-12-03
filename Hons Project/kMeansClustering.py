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


#onlySelectCentroidIfNearsestPointsIsEmpty means that thre needs to be nearest points already selected 
def getClosestCentroid(datapoint,centroidDatas,onlySelectCentroidIfNearsestPointsIsEmpty):
    closestCentroidData = []
    closestDistance = 9999999999.9
    for i in range(len(centroidDatas)):
        #distance = knn.distance(centroidDatas[i].centoid, datapoint)
        distance = utils.GetEuclideanDistanceBetweenFeatureVectors(kfold.getX(centroidDatas[i].centoid),kfold.getX(datapoint) )
        if( distance < closestDistance):
            #this centroid can oly be selected if nearest points exists. This is in the case for selecting centroids for testing data
            if onlySelectCentroidIfNearsestPointsIsEmpty:
                if not centroidDatas[i].nearestDataPoints.empty:
                    closestCentroidData = centroidDatas[i]
                    closestDistance = distance
                else:
                    uu = 0
            #select centroid regardless
            else:
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
            centroidData = getClosestCentroid( dataRow, centroidDatas, onlySelectCentroidIfNearsestPointsIsEmpty = False)
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

            #if no points are assosiated with the centroid then the centroid does not move
            if not centroidDatas[i].nearestDataPoints.empty:
                newCentroid = getMeanPoint(centroidDatas[i].nearestDataPoints,trainingData)
            else:
                newCentroid = centroidDatas[i].centoid
        
        
        
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

#cen = CalculateCentroids(kfold.testSet(1).trainingDF, k)


#trainingX = kfold.getX(ts.trainingDF).to_numpy()
#trainingY = kfold.getY(ts.trainingDF).to_numpy()
#testingX = kfold.getX(ts.testingDF).to_numpy()
#testingY = kfold.getY(ts.testingDF).to_numpy()


#results = ols.RunDataset( trainingY, trainingX, testingY, testingX)

def RunClustering(testSet, k, movingThreshold):
    centroidResults = CentroidResults()

    centroidDatas = getInitialCentroidDatas(k,testSet.trainingDF)  

    centroidDatas = CalculateCentroids(testSet.trainingDF, k, movingThreshold, centroidDatas)
    
    #associate testing data to centroids
    for i in range(len(testSet.testingDF)):
        dataRow = testSet.testingDF.iloc[i]
        centroidData = getClosestCentroid( dataRow, centroidDatas, onlySelectCentroidIfNearsestPointsIsEmpty = True)
        centroidData.nearestDataPointsTempListForTestingData.append(dataRow)
    
    for i in range(k):
        centroidDatas[i].testingData = pd.DataFrame(centroidDatas[i].nearestDataPointsTempListForTestingData, columns=testSet.testingDF.columns)

        trainingX = kfold.getX(centroidDatas[i].nearestDataPoints).to_numpy()
        trainingY = kfold.getY(centroidDatas[i].nearestDataPoints).to_numpy()
        testingX = kfold.getX(centroidDatas[i].testingData).to_numpy()
        testingY = kfold.getY(centroidDatas[i].testingData).to_numpy()
        
        #training data and testing data has to be available for the OLS regression to run
        results = ols.OLSRun()
        if not centroidDatas[i].nearestDataPoints.empty and not centroidDatas[i].testingData.empty and ols.givesSingularMatrix(trainingX) == False:
            results = ols.RunDataset( trainingY, trainingX, testingY, testingX)

        #store centroid data in results
        centroidResults.centroidData.append(centroidDatas[i])
        #store results of running ols on the test data for that centroid
        centroidResults.olsRuns.append( results )
    return centroidResults


#l = getKCentroids(2)

#a = randomN()

#dist = utils.GetEuclideanDistanceBetweenFeatureVectors( a, x_df.head(1).to_numpy())






#b = 1