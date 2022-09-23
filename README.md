# Guvi_PythonSeleniumProject_1

**Python 3.x**   

**Packages required:**
  - [pytest](https://pypi.org/project/pytest/)
  - [selenium](https://pypi.org/project/selenium/)


**Testing:**  
  - Clone the repository.  
  - Download and install Python 3.x version.
  - Install pytest and selenium packages.
  - Go to the cloned repository and update the details in **_config/data.json_** file:
```
{
  "url": "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
  "user": "Admin",
  "password": "admin123",
  "users" : [{
      "name": "Albert Einstein",
      "emp_id": 343,
      "user_name": "alberteinstein",
      "password": "Albert@343"
  }]
}
```

  - Run the below command to run the tests:   
    **pytest -s -v**
   

``` PS F:\workspace\Guvi_PythonSeleniumProject_1> pytest -s -v
====================================================================== test session starts =======================================================================
platform win32 -- Python 3.10.6, pytest-7.1.2, pluggy-1.0.0 -- C:\Users\DELL\AppData\Local\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.10.6', 'Platform': 'Windows-10-10.0.18363-SP0', 'Packages': {'pytest': '7.1.2', 'py': '1.11.0', 'pluggy': '1.0.0'}, 'Plugins': {'html': '3.
1.1', 'html-reporter': '0.2.9', 'metadata': '2.0.2'}}
rootdir: F:\workspace\Guvi_PythonSeleniumProject_1
plugins: html-3.1.1, html-reporter-0.2.9, metadata-2.0.2
collected 7 items                                                                                                                                                 

test_user_management_tool.py::Test1::test_1_login PASSED
test_user_management_tool.py::Test1::test_2_add_employee PASSED
test_user_management_tool.py::Test1::test_3_save_employee_details PASSED
test_user_management_tool.py::Test1::test_4_add_user PASSED
test_user_management_tool.py::Test1::test_5_find_user PASSED
test_user_management_tool.py::Test1::test_6_logout_user PASSED
test_user_management_tool.py::Test1::test_7_relogin_with_user PASSED

================================================================== 7 passed in 99.24s (0:01:39) ================================================================== ```
