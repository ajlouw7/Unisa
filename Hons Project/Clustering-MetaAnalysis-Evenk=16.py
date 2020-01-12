import math
import pandas as pd
import Utils as utils
import kNN as kNN
import kfold as kfold
import csv
import seaborn as sns

analysisdf = pd.DataFrame( columns=['dataset','fold','k','Average Mean Error','Average stdDev'])

index = 0

for dataset in range(1,11):
    for fold in range(1,11):
        fileName = 'Analysis\\Cluster-Analysis-Even-Fold' + str(fold) + 'theshold0.001noCentroids=16-Run' + str(dataset) + '.csv'
        df = pd.read_csv(fileName)
        index = index + 1
        analysisdf.at[index,'dataset'] = dataset
        analysisdf.at[index,'fold'] = fold
        analysisdf.at[index,'k'] = df['k'].mean()
        analysisdf.at[index,'Average Mean Error'] = df['Mean'].mean()
        analysisdf.at[index,'Average stdDev'] = df['stdDev'].mean()


analysisdf.to_csv('Analysis\\Clustering-MetaAnalysis-Even16.csv')

df= pd.read_csv('Analysis\\Clustering-MetaAnalysis-Even16.csv')

finalAnalysisDF = pd.DataFrame(  columns=['dataset','k','Average Mean Error','Average stdDev'])
for dataset in range(1,11):
    #create new dataframe of just this k
    perKDF = df.loc[df['dataset'] == dataset]
    index = index + 1
    finalAnalysisDF.at[index,'dataset'] = dataset
    finalAnalysisDF.at[index,'k'] = perKDF['k'].mean()
    finalAnalysisDF.at[index,'Average Mean Error'] = perKDF['Average Mean Error'].mean()
    finalAnalysisDF.at[index,'Average stdDev'] = perKDF['Average stdDev'].mean()

finalAnalysisDF.to_csv('Analysis\\Clustering-MetaAnalysis-Even16-Final.csv')




