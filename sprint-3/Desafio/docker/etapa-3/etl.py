import pandas as pd

df = pd.read_csv('concert_tours_by_women.csv')

df.drop_duplicates()
df.drop(['Ref.', 'Peak', 'All Time Peak'], axis=1, inplace=True)

df[['Start Year', 'End Year']] = df['Year(s)'].str.extract(r'(\d{4})-?(\d{4})?')
df['Start Year'] = pd.to_numeric(df['Start Year'])
df['End Year'] = pd.to_numeric(df['End Year'])
df['End Year'] = df['End Year'].fillna(df['Start Year'])

df.drop(['Year(s)'], axis=1, inplace=True)

df['Actual gross'] = df['Actual gross'].str.replace('$', '', regex=False)
df['Actual gross'] = df['Actual gross'].str.replace(',', '', regex=False)
df['Actual gross'] = df['Actual gross'].str.replace(r'\[.*\]', '', regex=True)
df['Actual gross']= pd.to_numeric(df['Actual gross'], errors='coerce')

df['Average gross'] = df['Average gross'].str.replace('$', '', regex=False)
df['Average gross'] = df['Average gross'].str.replace(',', '', regex=False)
df['Average gross'] = df['Average gross'].str.replace(r'\[.*\]', '', regex=True)
df['Average gross']= pd.to_numeric(df['Average gross'], errors='coerce')

df['Adjustedgross (in 2022 dollars)'] = df['Adjustedgross (in 2022 dollars)'].str.replace('$', '', regex=False)
df['Adjustedgross (in 2022 dollars)'] = df['Adjustedgross (in 2022 dollars)'].str.replace(',', '', regex=False)
df['Adjustedgross (in 2022 dollars)'] = df['Adjustedgross (in 2022 dollars)'].str.replace(r'\[.*\]', '', regex=True)
df['Adjustedgross (in 2022 dollars)']= pd.to_numeric(df['Adjustedgross (in 2022 dollars)'], errors='coerce')

df['Tour title'] = df['Tour title'].str.replace(r'(?<=Tour).*', '', regex=True)
df['Tour title'] = df['Tour title'].str.replace('†', '', regex=False)

df['Shows'] = pd.to_numeric(df['Shows'], errors='coerce')

print(df)

df.to_csv('output/csv_limpo.csv', index=False)
