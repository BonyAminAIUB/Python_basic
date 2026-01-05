import pandas as pd

df = pd.read_csv('/california_housing_test.csv')
# df.head()
# df.info()
df.describe() # count, mean, max, min ber kore dey

df.dropna()  # je sob value null lekha thakbe tader delete kore dibe

df.head() # je sokol null value thakbe tader puro row ke clean kore dibe

df = df.drop(['Student_ID'],axis=1) # Student_ID column delete kore dibe
# axis = 1 means column borabor delete hobe
# axis = 0 means row borabor delete hobe
df.head()

df = df[df['Math'] > 70] # jader mark 70 er niche tara delete hoye jabe
df.head()

df['Total'] = df[['English', 'Math', 'Bengali']].sum(axis=1) # new ekta column add hobe 'Total' name jekhane sum dekhabe
df.head()
