from core.reader_factory import get_reader
from core.validators import *
from utils.excel_utils import read_expectations
from datetime import datetime

# GX-style rules
def expect_not_null(df, column, _=None): return df[column].notnull().all()
def expect_unique(df, column, _=None): return df[column].is_unique
def expect_min_value(df, column, value): return (df[column] >= float(value)).all()
def expect_allowed_values(df, column, values): return df[column].isin(values.split(",")).all()

RULE_REGISTRY = {
    "not_null": expect_not_null,
    "unique": expect_unique,
    "min_value": expect_min_value,
    "allowed_values": expect_allowed_values
}

class TestExecutor:
    def __init__(self):
        self.results = []

    def execute(self, test_case):
        src_reader = get_reader(test_case["source_type"], test_case["source_details"])
        tgt_reader = get_reader(test_case["target_type"], test_case["target_details"])
        src_df = src_reader.read()
        tgt_df = tgt_reader.read()

        status = True
        messages = []

        # Smoke test: count check
        if test_case["run_type"] == "SMOKE":
            if not count_check(src_df, tgt_df):
                status = False
                messages.append("Count mismatch (Smoke)")

        # Regression tests
        if test_case["run_type"] == "REGRESSION":
            if not count_check(src_df, tgt_df):
                status = False
                messages.append("Count mismatch")
            if not duplicate_check(tgt_df, test_case["primary_key"]):
                status = False
                messages.append("Duplicate PK")
            if not incremental_check(src_df, tgt_df, test_case.get("incremental_column")):
                status = False
                messages.append("Incremental failure")

        # GX-style expectations
        expectations = [e for e in read_expectations() if e["table_name"] == test_case["table_name"]]
        for e in expectations:
            rule_func = RULE_REGISTRY[e["rule_type"]]
            if not rule_func(tgt_df, e["column_name"], e.get("rule_value")):
                status = False
                messages.append(f"Expectation failed: {e['rule_type']} on {e['column_name']}")

        self.results.append({
            "test_id": test_case["test_id"],
            "table": test_case["table_name"],
            "status": "PASS" if status else "FAIL",
            "messages": "; ".join(messages),
            "run_date": datetime.now()
        })
