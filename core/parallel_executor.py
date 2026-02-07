from concurrent.futures import ThreadPoolExecutor

def run_parallel(test_cases, executor, workers=5):
    with ThreadPoolExecutor(max_workers=workers) as pool:
        pool.map(executor.execute, test_cases)
