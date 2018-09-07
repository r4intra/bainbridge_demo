from code.utils.csv_loader import CSVtoDataFrameHelper
from code.models.event import EventFlatFileForTableau
from glob import glob

file_list = glob('/Users/shaunwalters/bainbridge_demo/code/resources/faers_ascii_2018q2/ascii/*.txt')

print(file_list)

test = EventFlatFileForTableau(file_list[0:5], 'DEMO18Q2')

print(test)

#
# test = CSVtoDataFrameHelper('/Users/shaunwalters/bainbridge_demo/code/resources/faers_ascii_2018q2/ascii/DEMO18Q2.txt')
#
# print(test.data['DEMO18Q2'].groupby(level=0).caseversion.count().sort_values(ascending=False).head())