import kfold as kfold
import kMeansClustering as cluster
import csv


#i=1
#k=5
movingThreshold= 0.001 


#results[centroidIndex].centroidData
#results[centroidIndex].olsRuns.results
for i in range(1,11):
    for k in range(2,10):
        results = cluster.RunClustering(kfold.testSet(i), k, movingThreshold )
        for centroidIndex in range(k):
            fileName = 'Cluster_Results' + str(i) + 'cluster=' + str(centroidIndex) + 'of' + str(k) + ' theshold= ' + str(movingThreshold) + '.csv'
            with open(fileName,mode='w', newline='') as resultsFile:
                resultsWriter = csv.writer( resultsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                resultsWriter.writerow(['LE','Predicted LE', 'Error','Health_Expenditure','GDP_Per_Capita','Education','Unemployment'])
                for r in results.olsRuns[centroidIndex].results:   
                    resultsWriter.writerow([float(r.lifeExpectancy), float(r.predictedLifeExpectancy), float(r.error), r.inputFeatureVector[0], r.inputFeatureVector[1],r.inputFeatureVector[2],r.inputFeatureVector[3]])

l = 0

