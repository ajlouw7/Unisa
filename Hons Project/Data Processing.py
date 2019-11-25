import pandas as pd

def getUnpivotetDF(df,pd, indicatorName):
    return pd.melt(df, 
                    id_vars=['Country_Name'],
                    value_vars=['1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018'], 
                    var_name='Year',
                    value_name=indicatorName)


lifeExpectancy_df = pd.read_csv("DataSet\Life Expectancy.csv")
upPivotedLifeExpectacy_df = getUnpivotetDF(lifeExpectancy_df,pd,'Life_Expectancy')
upPivotedLifeExpectacy_df.to_csv("Unpivotet Life Expectancy.csv")                            

#adultLiteracy_df = pd.read_csv("DataSet\Adult Litracy.csv")
#upPivotedAdultLiteracy_df= getUnpivotetDF(adultLiteracy_df, pd,'Adult Literacy') 
#upPivotedAdultLiteracy_df.to_csv("Unpivotet Adult Literacy.csv")

healthExpenditure_df = pd.read_csv("DataSet\Health Expediture.csv")
unPivotedHealthExpenditure_df = getUnpivotetDF(healthExpenditure_df,pd,'Health_Expenditure')
unPivotedHealthExpenditure_df.to_csv("Unpivotet Health Expenditure.csv")

gdpPerCapita_df = pd.read_csv("DataSet\GDP per Capita.csv")
unPivotedgdpPerCapita_df = getUnpivotetDF(gdpPerCapita_df,pd,'GDP_Per_Capita')
unPivotedgdpPerCapita_df.to_csv("Unpivotet GDP per Capita.csv")

primarySchoolEnrollment_df = pd.read_csv("DataSet\Primary school enrollment.csv")
unPivotedPrimarySchoolEnrollment_df = getUnpivotetDF(primarySchoolEnrollment_df,pd,'Primary_School_Enrollment')
unPivotedPrimarySchoolEnrollment_df.to_csv("Unpivotet Primary School Enrollment.csv")

secondaySchoolEnrollment_df = pd.read_csv("DataSet\Secondary School Enrollment.csv")
unPivotedSecondaySchoolEnrollment_df = getUnpivotetDF(secondaySchoolEnrollment_df,pd,'Secondary_School_Enrollment')
unPivotedSecondaySchoolEnrollment_df.to_csv("Unpivotet Secondary School Enrollment.csv")

tertiarySchoolEnrollment_df = pd.read_csv("DataSet\Tertiary School Enrollment.csv")
unPivotedTertiarySchoolEnrollment_df = getUnpivotetDF(tertiarySchoolEnrollment_df,pd,'Tertiary_School_Enrollment')
unPivotedTertiarySchoolEnrollment_df.to_csv("Unpivotet Tertiary School Enrollment.csv")

unemployment_df = pd.read_csv("DataSet\\Unemployment.csv")
unPivotedUnemployment_df = getUnpivotetDF(unemployment_df,pd,'Unemployment')
unPivotedUnemployment_df.to_csv("Unpivotet Unemployment.csv")


def mergeIndicators(df1,df2):
    return pd.merge(df1, df2, on = ["Country_Name","Year"] )

#new_df = pd.merge(upPivotedLifeExpectacy_df, upPivotedAdultLiteracy_df, on = ["Country Name","Year"] )
merged_df = mergeIndicators( upPivotedLifeExpectacy_df, unPivotedHealthExpenditure_df )
merged_df = mergeIndicators( merged_df,unPivotedgdpPerCapita_df )
merged_df = mergeIndicators( merged_df,unPivotedPrimarySchoolEnrollment_df )
merged_df = mergeIndicators( merged_df,unPivotedSecondaySchoolEnrollment_df )
merged_df = mergeIndicators( merged_df,unPivotedTertiarySchoolEnrollment_df )
merged_df = mergeIndicators( merged_df,unPivotedUnemployment_df )
merged_df = merged_df.dropna(subset=['Life_Expectancy', 'Health_Expenditure','GDP_Per_Capita','Primary_School_Enrollment','Secondary_School_Enrollment','Tertiary_School_Enrollment','Unemployment'])

merged_df = merged_df[merged_df['Country_Name'] != 'Europe & Central Asia (IDA & IBRD countries)']
merged_df = merged_df[merged_df['Country_Name'] != 'Post-demographic dividend']
merged_df = merged_df[merged_df['Country_Name'] != 'Late-demographic dividend']
merged_df = merged_df[merged_df['Country_Name'] != 'Early-demographic dividend']
merged_df = merged_df[merged_df['Country_Name'] != 'OECD members']
merged_df = merged_df[merged_df['Country_Name'] != 'Middle East & North Africa (IDA & IBRD countries)']
merged_df = merged_df[merged_df['Country_Name'] != 'Middle East & North Africa (excluding high income)']
merged_df = merged_df[merged_df['Country_Name'] != 'Middle East & North Africa']
merged_df = merged_df[merged_df['Country_Name'] != 'Latin America & the Caribbean (IDA & IBRD countries)']
merged_df = merged_df[merged_df['Country_Name'] != 'Latin America & Caribbean (excluding high income)']
merged_df = merged_df[merged_df['Country_Name'] != 'Latin America & Caribbean']
merged_df = merged_df[merged_df['Country_Name'] != 'European Union']
merged_df = merged_df[merged_df['Country_Name'] != 'Europe & Central Asia']
merged_df = merged_df[merged_df['Country_Name'] != 'Europe & Central Asia (excluding high income)']
merged_df = merged_df[merged_df['Country_Name'] != 'Caribbean small states']
merged_df = merged_df[merged_df['Country_Name'] != 'Central Europe and the Baltics']
merged_df = merged_df[merged_df['Country_Name'] != 'Arab World']
merged_df = merged_df[merged_df['Country_Name'] != 'North America']
merged_df = merged_df[merged_df['Country_Name'] != 'IDA blend']
merged_df = merged_df[merged_df['Country_Name'] != 'East Asia & Pacific (IDA & IBRD countries)']
merged_df = merged_df[merged_df['Country_Name'] != 'East Asia & Pacific (excluding high income)']
merged_df = merged_df[merged_df['Country_Name'] != 'Upper middle income']
merged_df = merged_df[merged_df['Country_Name'] != 'High income']
merged_df = merged_df[merged_df['Country_Name'] != 'Lower middle income']
merged_df = merged_df[merged_df['Country_Name'] != 'Low & middle income']
merged_df = merged_df[merged_df['Country_Name'] != 'Euro area']
merged_df = merged_df[merged_df['Country_Name'] != 'South Asia (IDA & IBRD)']
merged_df = merged_df[merged_df['Country_Name'] != 'IDA & IBRD total']
merged_df = merged_df[merged_df['Country_Name'] != 'IBRD only']
merged_df = merged_df[merged_df['Country_Name'] != 'World']


def NormaliseColumn(df,columnName):
    columnMax = df[columnName].max()
    columnMin = df[columnName].min()
    df[columnName] = (df[columnName]-columnMin )/( columnMax - columnMin)

raw_df = merged_df
raw_df['Education'] =  (raw_df['Primary_School_Enrollment'] + raw_df['Secondary_School_Enrollment'] + raw_df['Tertiary_School_Enrollment'])/3
raw_df.to_csv("raw.csv")


NormaliseColumn(merged_df,'GDP_Per_Capita')
NormaliseColumn(merged_df,'Health_Expenditure')
NormaliseColumn(merged_df,'Primary_School_Enrollment')
NormaliseColumn(merged_df,'Secondary_School_Enrollment')
NormaliseColumn(merged_df,'Tertiary_School_Enrollment')
NormaliseColumn(merged_df,'Unemployment')

merged_df['Education'] =  (merged_df['Primary_School_Enrollment'] + merged_df['Secondary_School_Enrollment'] + merged_df['Tertiary_School_Enrollment'])/3


# output data to file
merged_df.to_csv("test.csv")

sorted_df = merged_df
sorted_df = sorted_df.sort_values(by='Life_Expectancy', ascending = False)

sorted_df.to_csv("sorted.csv")

count = 1062
half = (int)(count/2)

top_df = sorted_df.head(half)
top_df.to_csv("top.csv")

bottom_df = sorted_df.tail(half)
bottom_df.to_csv("bottom.csv")

topSample = top_df.sample(n=53)
bottomSample = bottom_df.sample(n=53)

df1 = pd.concat([topSample, bottomSample ], ignore_index=True)
df1.to_csv("df1.csv")

topSample = top_df.sample(n=53)
bottomSample = bottom_df.sample(n=53)

df2 = pd.concat([topSample, bottomSample ], ignore_index=True)
df2.to_csv("df2.csv")

topSample = top_df.sample(n=53)
bottomSample = bottom_df.sample(n=53)

df3 = pd.concat([topSample, bottomSample ], ignore_index=True)
df3.to_csv("df3.csv")

topSample = top_df.sample(n=53)
bottomSample = bottom_df.sample(n=53)

df4 = pd.concat([topSample, bottomSample ], ignore_index=True)
df4.to_csv("df4.csv")

topSample = top_df.sample(n=53)
bottomSample = bottom_df.sample(n=53)

df5 = pd.concat([topSample, bottomSample ], ignore_index=True)
df5.to_csv("df5.csv")

topSample = top_df.sample(n=53)
bottomSample = bottom_df.sample(n=53)

df6 = pd.concat([topSample, bottomSample ], ignore_index=True)
df6.to_csv("df6.csv")

topSample = top_df.sample(n=53)
bottomSample = bottom_df.sample(n=53)

df7 = pd.concat([topSample, bottomSample ], ignore_index=True)
df7.to_csv("df7.csv")

topSample = top_df.sample(n=53)
bottomSample = bottom_df.sample(n=53)

df8 = pd.concat([topSample, bottomSample ], ignore_index=True)
df8.to_csv("df8.csv")

topSample = top_df.sample(n=53)
bottomSample = bottom_df.sample(n=53)

df9 = pd.concat([topSample, bottomSample ], ignore_index=True)
df9.to_csv("df9.csv")

topSample = top_df.sample(n=53)
bottomSample = bottom_df.sample(n=53)

df10 = pd.concat([topSample, bottomSample ], ignore_index=True)
df10.to_csv("df10.csv")

print ("hello")


