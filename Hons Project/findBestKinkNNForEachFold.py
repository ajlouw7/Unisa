import math
import pandas as pd
import Utils as utils
import kNN as kNN
import kfold as kfold
import csv
import seaborn as sns

analysis_df = pd.read_csv('Analysis\\kNN-Analysis.csv')
newDF = pd.DataFrame(columns=analysis_df.columns)

for i in range(1,11):
    df = analysis_df.loc[analysis_df['Series'] == i]
    a = df[df.Mean == df.Mean.min()]

    newDF = newDF.append(a,ignore_index = True)
       
       
   

newDF.to_csv('Analysis\\kNN-Analysis-FoundBestK.csv')