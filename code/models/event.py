import pandas as pd

from typing import List, Dict
from code.utils.csv_loader import CSVtoDataFrameHelper


class EventFlatFileForTableau(object):

    def __init__(self, files: List[str], event_file: str) -> None:
        self.files = files
        self.event_file = event_file
        self.inventory = self.load_dataframes()
        self.flat = self.assemble_flat_file()

    def __repr__(self):
        return self.flat.info()

    def load_dataframes(self) -> Dict:

        data_list = [CSVtoDataFrameHelper(f).data for f in self.files]
        df_dict = {}
        for d in data_list:
            df_dict = {**df_dict, **d}
        return df_dict

    def assemble_flat_file(self) -> pd.DataFrame:

        leader = self.inventory[self.event_file]
        frames = [self.inventory[x] for x in self.inventory.keys() if x != self.event_file]

        return leader.join(frames)
