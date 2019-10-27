import pandas as pd
import math
import kNN as KNN



df = pd.read_csv("test.csv")
rrs = KNN.getKNN(df, df.head(1),3)
av = KNN.avgOfKNN(df,df.head(1),3)



i = 0




 #   data.