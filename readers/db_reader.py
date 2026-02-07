import pandas as pd
from core.base_reader import BaseReader
from sqlalchemy import create_engine
import yaml

class DBReader(BaseReader):
    def __init__(self, table_name, db_name="default_db"): self.table_name = table_name; self.db_name = db_name
    def read(self):
        with open("config/db_config.yaml") as f: cfg = yaml.safe_load(f)
        engine = create_engine(cfg[self.db_name]["connection"])
        return pd.read_sql(f"SELECT * FROM {self.table_name}", engine)
