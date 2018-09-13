import pandas as pd

path = '/Users/shaunwalters/Desktop/'


# ATC.csv
df = pd.read_csv(path + 'atc.txt', sep='|', usecols=[12, 13, 14], names=['tty', 'code', 'name'])

df[df.tty == 'PT'].drop_duplicates().to_csv(path + 'atc.csv', index=False)

# ATC Mapping.csv
df2 = pd.read_csv(path + 'atc_mapping.csv')
df2['atc_group_4'] = df2.atc_code.str[0:5]
df2['atc_group_3'] = df2.atc_code.str[0:4]
df2['atc_group_2'] = df2.atc_code.str[0:3]
df2['atc_group_1'] = df2.atc_code.str[0:1]
df2.to_csv(path + 'atc_mapping.csv', index=False)