from utils.excel_utils import read_test_cases
from core.test_executor import TestExecutor
from core.parallel_executor import run_parallel
from reports.html_reporter import generate_html

executor = TestExecutor()
tests = [t for t in read_test_cases() if t["run_type"]=="REGRESSION"]

run_parallel(tests, executor, workers=5)
generate_html(executor.results)
print("Regression tests complete. Report at reports/etl_report.html")
