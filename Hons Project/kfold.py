import pandas as pd

class TestSet:
    def __init__(self):
        self.trainingDF = []
        self.testingDF = []

def getX(df):
    return df[['Health_Expenditure','GDP_Per_Capita','Education','Unemployment']]
    
def path(dataset):
    return "PreparedDatasets\Dataset" + str(dataset) + "\\"


def getY(df):
    return df[['Life_Expectancy']]

def create_df1(dataset):
    return pd.read_csv(path(dataset) + "df1.csv")

def create_df2(dataset):
    return pd.read_csv(path(dataset) + "df2.csv")

def create_df3(dataset):
    return pd.read_csv(path(dataset) + "df3.csv")

def create_df4(dataset):
    return pd.read_csv(path(dataset) + "df4.csv")

def create_df5(dataset):
    return pd.read_csv(path(dataset) + "df5.csv")

def create_df6(dataset):
    return pd.read_csv(path(dataset) + "df6.csv")

def create_df7(dataset):
    return pd.read_csv(path(dataset) + "df7.csv")

def create_df8(dataset):
    return pd.read_csv(path(dataset) + "df8.csv")

def create_df9(dataset):
    return pd.read_csv(path(dataset) + "df9.csv")

def create_df10(dataset):
    return pd.read_csv(path(dataset) + "df10.csv")

def create_df(fold,dataset):
    if( fold == 1):
        return create_df1(dataset)
    elif( fold == 2 ):
        return create_df2(dataset)
    elif( fold == 3 ):
        return create_df3(dataset)
    elif( fold == 4 ):
        return create_df4(dataset)
    elif( fold == 5 ):
        return create_df5(dataset)
    elif( fold == 6 ):
        return create_df6(dataset)
    elif( fold == 7 ):
        return create_df7(dataset)
    elif( fold == 8 ):
        return create_df8(dataset)
    elif( fold == 9 ):
        return create_df9(dataset)
    elif( fold == 10 ):
        return create_df10(dataset)
    
def testSet(fold,dataset):
    ts = TestSet()
    ts.testingDF = create_df(fold,dataset)
    isTrainingDFSet = False
    for j in range(1,10):
        #look for dataset with index that is not the same as the index of the testing set 
        if fold != j:
            if not isTrainingDFSet:
                #create the start of the training set
                isTrainingDFSet = True
                ts.trainingDF = create_df(j,dataset)
            else:
                #append the other folds to make up the training set
                ts.trainingDF = pd.concat([ts.trainingDF, create_df(j,dataset) ], ignore_index=True)
    return ts
