# Allure report generation
# pip install allure-pytest

pytest -s -q --alluredir allure_results/json
allure generate allure_results/json -o allure_results/html
allure generate allure_results/json -o allure_results/html --clean
# can open the report from the browser itself
# no need to allure serve


# Pytest normal approach
# pytest --alluredir=allure_results
# pytest --alluredir=allure_results test_execute_testcsv.py
# allure serve


pytest test_tc1_execute_testcsv.py --log-format="%(asctime)s %(levelname)s %(message)s" \ --log-date-format="%Y-%m-%d %H:%M:%S"

pytest test_tc1_execute_testcsv.py