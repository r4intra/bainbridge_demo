from code.utils.csv_loader import CSVtoDataFrameHelper

path = '/Users/shaunwalters/bainbridge_demo/code/resources/faers_ascii_2018q2/ascii/'

# DROP THERAPY AND INDICATIONS
files = ['DEMO18Q2.txt',
         'DRUG18Q2.txt',
         'REAC18Q2.txt',
         'OUTC18Q2.txt',
         'RPSR18Q2.txt']

file_list = [path + f for f in files]

for f in file_list:
    helper = CSVtoDataFrameHelper(f).data
    helper_name = [x for x in helper.keys()][0]
    df = helper[helper_name].to_csv('/Users/shaunwalters/Desktop/' + helper_name + '.csv')
