import os
import shutil
import pytest

if __name__ == "__main__":
    pytest.main()
    shutil.copy('./environment.xml', 'report/allure')
    os.system(f"allure serve ./report/allure")
