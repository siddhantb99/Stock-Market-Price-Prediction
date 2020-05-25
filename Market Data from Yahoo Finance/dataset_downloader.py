import os
import glob
import pandas as pd
from pandas_datareader import data

# open the companies name whose data is to be downloaded
df = pd.read_csv('companies.csv')

companies = list(df['0'])

def download_data(name):
  temp = name + '.NS'
  df = data.DataReader(temp, 'yahoo', '2015-01-01')
  file_name = name+'.csv'
  df.to_csv('data/'+file_name)
  df = pd.read_csv('data/'+file_name)
  df.insert(0,'ID',name)
  df.to_csv('data/'+file_name,index=False)

for name in companies:
  download_data(name)

## merging all the csv files in one csv file
os.chdir("data")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
all_data = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
all_data.to_csv( "all_data.csv", index=False, encoding='utf-8-sig')
