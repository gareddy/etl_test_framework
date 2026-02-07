from datetime import datetime

def generate_html(results):
    rows = ""
    for r in results:
        css = "pass" if r["status"]=="PASS" else "fail"
        rows += f"<tr class='{css}'><td>{r['test_id']}</td><td>{r['table']}</td><td>{r['status']}</td><td>{r['messages']}</td></tr>"

    html = f"""
    <html><head><title>ETL Report</title>
    <style>table{{border-collapse:collapse;}}th,td{{border:1px solid black;padding:5px;}}
    .pass{{background:#c8e6c9;}}.fail{{background:#ffcdd2;}}</style></head><body>
    <h2>ETL Test Execution Report</h2>
    <p>Date: {datetime.now()}</p>
    <table><tr><th>Test ID</th><th>Table</th><th>Status</th><th>Messages</th></tr>{rows}</table>
    </body></html>"""

    with open("reports/etl_report.html","w") as f: f.write(html)
