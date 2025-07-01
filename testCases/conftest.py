# this file setup the environment for running tests with Selenium WebDriver.
# This file is used to configure pytest fixtures and options for running tests with Selenium WebDriver.

from selenium import webdriver
import pytest

@pytest.fixture()
# This is a pytest fixture that sets up the Chrome WebDriver before each test and tears it down after each test.
def setup(browser):
    global driver
    if browser == 'chrome':
        # You can add more browser options here if needed
        driver = webdriver.Chrome()
        print("Launching Chrome browser...")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser...")
    return driver


# This fixture can be used in test cases to get the WebDriver instance.
#  Calling `setup` will return a WebDriver instance that can be used in tests.

def pytest_addoption(parser):
    # This function adds a command line option to pytest to specify the browser type.
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type of browser to run tests on")  # Default is Chrome


@pytest.fixture()
def browser(request):
    # This fixture retrieves the browser type from the command line option and returns it.
    return request.config.getoption("--browser")


##### pytest HTML report #####

def pytest_html_report_title(report):
    report.title = "My Custom Report Title"


@pytest.mark.optionalhook
def pytest_configure(config):
    config._metadata = {
        "Project Name": "My Project",
        "Module Name": "Login",
        "Tester": "Shubham Pawar"
    }  # Module name for the report

    # @pytest.mark.optionalhook
    # def pytest_metadata(metadata):
    # This function is called to modify/delete the metadata in the HTML report.
    # metadata.pop('JAVA_HOME', None)  # Remove JAVA_HOME from metadata
    # metadata.pop('Plugins', None)  # Remove Plugins from metadata
# to generate html report, run the following command in terminal:
# pytest -s -v --html=Report\report.html testcase_address -- browser chrome
