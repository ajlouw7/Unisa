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

merged_df.to_csv("test.csv")
print ("hello")


