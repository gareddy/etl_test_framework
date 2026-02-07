import pandas as pd

def read_test_cases():
    df = pd.read_excel("control/etl_test_control.xlsx", sheet_name="test_cases")
    return df.to_dict(orient="records")

def read_expectations():
    df = pd.read_excel("control/etl_test_control.xlsx", sheet_name="expectations")
    return df.to_dict(orient="records")
