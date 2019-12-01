import pandas as pd
import numpy as np 
import Utils as utils
import OLS as ols
import kfold as kfold
import csv

analysisdf = pd.DataFrame( columns=['Series','Mean','stdDev'])

for i in range(1,11):
    ts = kfold.testSet(i)
    trainingX = kfold.getX(ts.trainingDF).to_numpy()
    trainingY = kfold.getY(ts.trainingDF).to_numpy()
    testingX = kfold.getX(ts.testingDF).to_numpy()
    testingY = kfold.getY(ts.testingDF).to_numpy()
    results = ols.RunDataset( trainingY, trainingX, testingY, testingX)
    fileName = 'OLS-Results\OLS_Results' + str(i) + '.csv'
    with open(fileName,mode='w', newline='') as resultsFile:
        resultsWriter = csv.writer( resultsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        resultsWriter.writerow(['LE','Predicted LE', 'Error','Health_Expenditure','GDP_Per_Capita','Education','Unemployment'])
        for r in results.results:   
            resultsWriter.writerow([float(r.lifeExpectancy), float(r.predictedLifeExpectancy), float(r.error), r.inputFeatureVector[0], r.inputFeatureVector[1],r.inputFeatureVector[2],r.inputFeatureVector[3]])
    df = pd.read_csv(fileName)
    analysisdf.at[i,'Series'] = i 
    analysisdf.at[i,'Mean'] = df['Error'].mean()
    analysisdf.at[i,'stdDev'] = df['Error'].std()
    pp=0

analysisdf.to_csv('Analysis\OlS-Analysis.csv')
j=9

