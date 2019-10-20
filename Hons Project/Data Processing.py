import pandas as pd

def getUnpivotetDF(df,pd, indicatorName):
    return pd.melt(df, 
                    id_vars=['Country Name'],
                    value_vars=['1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018'], 
                    var_name='Year',
                    value_name=indicatorName)


lifeExpectancy_df = pd.read_csv("DataSet\Life Expectancy.csv")
upPivotedLifeExpectacy_df = getUnpivotetDF(lifeExpectancy_df,pd,'Life Expectancy')
upPivotedLifeExpectacy_df.to_csv("Unpivotet Life Expectancy.csv")                            

adultLiteracy_df = pd.read_csv("DataSet\Adult Litracy.csv")
upPivotedAdultLiteracy_df= getUnpivotetDF(adultLiteracy_df, pd,'Adult Literacy') 
upPivotedAdultLiteracy_df.to_csv("Unpivotet Adult Literacy.csv")

healthExpenditure_df = pd.read_csv("DataSet\Health Expediture.csv")
unPivotedHealthExpenditure_df = getUnpivotetDF(healthExpenditure_df,pd,'Health Expenditure')
unPivotedHealthExpenditure_df.to_csv("Unpivotet Health Expenditure.csv")

gdpPerCapita_df = pd.read_csv("DataSet\GDP per Capita.csv")
unPivotedgdpPerCapita_df = getUnpivotetDF(gdpPerCapita_df,pd,'GDP Per Capita')
unPivotedgdpPerCapita_df.to_csv("Unpivotet GDP per Capita.csv")

primarySchoolEnrollment_df = pd.read_csv("DataSet\Primary school enrollment.csv")
unPivotedPrimarySchoolEnrollment_df = getUnpivotetDF(primarySchoolEnrollment_df,pd,'Primary Scool Enrollment')
unPivotedPrimarySchoolEnrollment_df.to_csv("Unpivotet Primary School Enrollment.csv")

secondaySchoolEnrollment_df = pd.read_csv("DataSet\Secondary School Enrollment.csv")
unPivotedSecondaySchoolEnrollment_df = getUnpivotetDF(secondaySchoolEnrollment_df,pd,'Secondary Scool Enrollment')
unPivotedSecondaySchoolEnrollment_df.to_csv("Unpivotet Secondary School Enrollment.csv")

tertiarySchoolEnrollment_df = pd.read_csv("DataSet\Tertiary School Enrollment.csv")
unPivotedTertiarySchoolEnrollment_df = getUnpivotetDF(tertiarySchoolEnrollment_df,pd,'Tertiary Scool Enrollment')
unPivotedTertiarySchoolEnrollment_df.to_csv("Unpivotet Tertiary School Enrollment.csv")

unemployment_df = pd.read_csv("DataSet\\Unemployment.csv")
unPivotedUnemployment_df = getUnpivotetDF(unemployment_df,pd,'Unemployment')
unPivotedUnemployment_df.to_csv("Unpivotet Unemployment.csv")


def mergeIndicators(df1,df2):
    return pd.merge(df1, df2, on = ["Country Name","Year"] )

#new_df = pd.merge(upPivotedLifeExpectacy_df, upPivotedAdultLiteracy_df, on = ["Country Name","Year"] )
merged_df = mergeIndicators( upPivotedLifeExpectacy_df, upPivotedAdultLiteracy_df )
merged_df = mergeIndicators( merged_df,unPivotedHealthExpenditure_df )
merged_df = mergeIndicators( merged_df,unPivotedgdpPerCapita_df )
merged_df = mergeIndicators( merged_df,unPivotedPrimarySchoolEnrollment_df )
merged_df = mergeIndicators( merged_df,unPivotedSecondaySchoolEnrollment_df )
merged_df = mergeIndicators( merged_df,unPivotedTertiarySchoolEnrollment_df )
merged_df = mergeIndicators( merged_df,unPivotedUnemployment_df )

merged_df.to_csv("test.csv")
print ("hello")


