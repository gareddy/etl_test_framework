from readers.csv_reader import CSVReader
from readers.db_reader import DBReader

def get_reader(reader_type, details):
    if reader_type.upper() == "CSV":
        return CSVReader(details)
    elif reader_type.upper() == "DB":
        return DBReader(details)
    else:
        raise Exception(f"Unsupported reader type: {reader_type}")
