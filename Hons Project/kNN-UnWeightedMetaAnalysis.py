import math
import pandas as pd
import Utils as utils
import kNN as kNN
import kfold as kfold
import csv
import seaborn as sns

analysisdf = pd.DataFrame( columns=['dataset','k','Average Mean Error','Average stdDev'])

index = 0

for dataset in range(1,11):
    fileName = 'Analysis\\kNN-Analysis-UnWeighted-Run' + str(dataset) + '.csv'
    df = pd.read_csv(fileName)
    for k in range(1,107):
        #create new dataframe of just this k
        perKDF = df.loc[df['k'] == k]
        index = index + 1
        analysisdf.at[index,'dataset'] = dataset
        analysisdf.at[index,'k'] = k 
        analysisdf.at[index,'Average Mean Error'] = perKDF['Mean'].mean()
        analysisdf.at[index,'Average stdDev'] = perKDF['stdDev'].mean()


analysisdf.to_csv('Analysis\\kNN-UnWeightedMetaAnalysis_Interim.csv')

resultdf = pd.DataFrame(columns=['dataset','k with min Average Mean Error','Average Mean Error at k','Average stdDev at k'])

for dataset in range(1,11):
    perDatasetDF = analysisdf.loc[analysisdf['dataset'] == dataset]
    minKdatarow = perDatasetDF[perDatasetDF['Average Mean Error'] == perDatasetDF['Average Mean Error'].min()]
    resultdf.at[dataset,'dataset']=dataset
    resultdf.at[dataset,'k with min Average Mean Error']=minKdatarow['k'].iloc[0]
    resultdf.at[dataset,'Average Mean Error at k']=minKdatarow['Average Mean Error'].iloc[0]
    resultdf.at[dataset,'Average stdDev at k']=minKdatarow['Average stdDev'].iloc[0]

resultdf.to_csv('Analysis\\kNN-UnWeightedMetaAnalysis.csv')


