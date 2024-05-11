import unittest
import time
from HTMLTestRunner import HTMLTestRunner

report_dir = 'test_report'
test_dir = 'test_cases'

print("start run test case")
discover = unittest.defaultTestLoader.discover(test_dir, "add_Commodity_Test.py")
row = time.strftime("%Y-%m-%d-%H-%M-%S")
report_name = report_dir + '/' + row + "result.html"
print("start write report..")
with open(report_name,"wb") as f:
    runner = HTMLTestRunner(stream=f,title="test_report",description="erp test")
    runner.run(discover)
    f.close()
print("test end")
