import os
import shutil
import pytest

if __name__ == "__main__":
    pytest.main()
    shutil.copy('/Users/ivi/Dev/apiTest/environment.xml', '/Users/ivi/Dev/apiTest/report/temp')
    os.system(f"allure serve /Users/ivi/Dev/apiTest/report/temp")
