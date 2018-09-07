import pandas as pd


class CSVtoDataFrameHelper(object):

    def __init__(self, fileloc):
        self.fileloc = fileloc
        self.csv_name = self.fileloc.split('/')[-1].split('.')[0]
        self.data = self.load_csv()

    def __repr__(self):
        return 'Keys: {}, Value: {}'.format([x for x in self.data.keys()],
                                            repr([x for x in self.data.values()])
                                            )

    def load_csv(self):
        init_df = pd.read_csv(self.fileloc, index_col=(0, 1), delimiter='$')
        print(self.csv_name + 'loaded.')
        print(init_df.info())
        return {self.csv_name: init_df}
