import pandas as pd
import math

def distance(p1,p2):
    squareDistance = 0
    squareDistance += math.pow(p1.Health_Expenditure - p2.Health_Expenditure,2)
    squareDistance += math.pow(p1.GDP_Per_Capita - p2.GDP_Per_Capita,2)
    squareDistance += math.pow(p1.Primary_School_Enrollment - p2.Primary_School_Enrollment,2)
    squareDistance += math.pow(p1.Secondary_School_Enrollment - p2.Secondary_School_Enrollment,2)
    squareDistance += math.pow(p1.Tertiary_School_Enrollment - p2.Tertiary_School_Enrollment,2)
    squareDistance += math.pow(p1.Unemployment - p2.Unemployment,2)
    
    return math.sqrt(squareDistance)

df = pd.read_csv("test.csv")

for p1 in df.head(1).itertuples():
    for p2 in df.itertuples():
        d = distance(p1,p2 )    
        print(d)

i = 0




 #   data.