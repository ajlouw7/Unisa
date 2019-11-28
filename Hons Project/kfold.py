import pandas as pd

class TestSet:
    def __init__(self):
        self.trainingDF = []
        self.testingDF = []

def getX(df):
    return df[['Health_Expenditure','GDP_Per_Capita','Education','Unemployment']]
    
def getY(df):
    return df[['Life_Expectancy']]

def create_df1():
    return pd.read_csv("df1.csv")

def create_df2():
    return pd.read_csv("df2.csv")

def create_df3():
    return pd.read_csv("df3.csv")

def create_df4():
    return pd.read_csv("df4.csv")

def create_df5():
    return pd.read_csv("df5.csv")

def create_df6():
    return pd.read_csv("df6.csv")

def create_df7():
    return pd.read_csv("df7.csv")

def create_df8():
    return pd.read_csv("df8.csv")

def create_df9():
    return pd.read_csv("df9.csv")

def create_df10():
    return pd.read_csv("df10.csv")

def create_df(i):
    if( i == 1):
        return create_df1()
    elif( i == 2 ):
        return create_df2()
    elif( i == 3 ):
        return create_df3()
    elif( i == 4 ):
        return create_df4()
    elif( i == 5 ):
        return create_df5()
    elif( i == 6 ):
        return create_df6()
    elif( i == 7 ):
        return create_df7()
    elif( i == 8 ):
        return create_df8()
    elif( i == 9 ):
        return create_df9()
    elif( i == 10 ):
        return create_df10()
    
def testSet(i):
    ts = TestSet()
    ts.testingDF = create_df(i)
    isTrainingDFSet = False
    for j in range(1,10):
        #look for dataset with index that is not the same as the index of the testing set 
        if i != j:
            if not isTrainingDFSet:
                #create the start of the training set
                isTrainingDFSet = True
                ts.trainingDF = create_df(j)
            else:
                #append the other folds to make up the training set
                ts.trainingDF = pd.concat([ts.trainingDF, create_df(j) ], ignore_index=True)
    return ts
