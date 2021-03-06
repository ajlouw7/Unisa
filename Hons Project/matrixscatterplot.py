import seaborn as sns
import pandas as pd

df = pd.read_csv("raw.csv")
df= df[['Life_Expectancy','Health_Expenditure','GDP_Per_Capita','Education','Unemployment']]

sns.set(style="ticks", color_codes=True)
g = sns.pairplot(df, diag_kind="kde")
g.savefig("matrixScatterPlot.png")
i = 0