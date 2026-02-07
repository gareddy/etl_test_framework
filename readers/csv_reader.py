import pandas as pd
from core.base_reader import BaseReader

class CSVReader(BaseReader):
    def __init__(self, path): self.path = path
    def read(self): return pd.read_csv(self.path)
