import pandas as pd
import kfold as kfold
import kMeansClustering as cluster
import csv


#i=1
#k=5
movingThreshold= 0.001
index = 0
delta = 1

analysisdf = pd.DataFrame( columns=['Series','k','delta','centroidNum','Mean','stdDev','count'])

numberOfCentroids = cluster.getK(delta)

for dataset in range(8,10):
    #for each fold
    for fold in range(1,11): #11   6,11
        #for each number of clusters
        for k in range(numberOfCentroids,numberOfCentroids+1): #2,16  1296,1297
            results = cluster.RunClustering(kfold.testSet(fold,dataset), k, movingThreshold, delta )
            #for each centroid    
            fileName = 'Cluster-Results\Cluster_Results-Fold' + str(fold) + '#ofclusters=' + str(k) + ' theshold= ' + str(movingThreshold) + 'dataset' +str(dataset)+ '.csv'
            with open(fileName,mode='w', newline='') as resultsFile:
                resultsWriter = csv.writer( resultsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                resultsWriter.writerow(['LE','Predicted LE', 'Error','Health_Expenditure','GDP_Per_Capita','Education','Unemployment','centroid#','centroid_Health_Expenditure','centroid_GDP_Per_Capita','centroid_Education','centroid_Unemployment'])
                for centroidIndex in range(k):
                    he = results.centroidData[centroidIndex].centoid.at[0,'Health_Expenditure']
                    gdp = results.centroidData[centroidIndex].centoid.at[0,'GDP_Per_Capita']
                    edu = results.centroidData[centroidIndex].centoid.at[0,'Education']
                    unem = results.centroidData[centroidIndex].centoid.at[0,'Unemployment']
                    for r in results.olsRuns[centroidIndex].results:   
                        resultsWriter.writerow([float(r.lifeExpectancy), float(r.predictedLifeExpectancy), float(r.error), r.inputFeatureVector[0], r.inputFeatureVector[1],r.inputFeatureVector[2],r.inputFeatureVector[3], str(centroidIndex + 1),float(he),float(gdp),float(edu),float(unem)])
            df = pd.read_csv(fileName)
            for centroidNum in range(1,k+1):
                index =  index +1
                analysisdf.at[index,'Series'] = fold
                analysisdf.at[index,'k'] = k 
                analysisdf.at[index,'delta'] = delta
                analysisdf.at[index,'centroidNum'] = centroidNum
                filtereddf = df.where( df['centroid#'] == centroidNum )
                analysisdf.at[index,'Mean'] = filtereddf['Error'].mean()
                analysisdf.at[index,'stdDev'] = filtereddf['Error'].std()
                analysisdf.at[index,'count'] = filtereddf['Error'].count()
        analysisdf.to_csv('Analysis\Cluster-Analysis-Even-Fold' + str(fold) + 'theshold' + str(movingThreshold) + 'noCentroids=' + str(numberOfCentroids) + '-Run' + str(dataset) + '.csv')
        #clear dataframe
        analysisdf = pd.DataFrame(columns=analysisdf.columns)
l = 0

