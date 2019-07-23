import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en-gb, ru, fr, de, es, it, sk, pt")

@pytest.fixture(scope="function")
def browser(request):
    lan = request.config.getoption("language")
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)  
    link = "http://selenium1py.pythonanywhere.com/"+lan+"/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    yield browser
    print("\nquit browser..")
    browser.quit()
    
