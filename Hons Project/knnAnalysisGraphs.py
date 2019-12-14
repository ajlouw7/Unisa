import math
import pandas as pd
import Utils as utils
import kNN as kNN
import kfold as kfold
import csv
import seaborn as sns

df = pd.read_csv('Analysis\\kNN-Analysis.csv')

k=10
#for k in range(1,11):

seriesData = df.loc[df['Series'] == k]
#seriesData = df

seriesData = seriesData.rename(columns={"Mean": "Mean Error in Predicted Life Expectancy"})

fileName = "kNNErrorPlot\kNNErrorPlot" + str(k) + ".png"

#fileName = "kNNErrorPlot\kNNErrorPlot.png"

sns.lineplot( x='k', y='Mean Error in Predicted Life Expectancy',ci="sd", data=seriesData).get_figure().savefig(fileName)

l=0
