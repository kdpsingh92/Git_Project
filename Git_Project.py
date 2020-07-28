from selenium import webdriver
import time
import random

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome( executable_path = "./chromedriver.exe", options=options )

username = "xxxxxx"
password = "yyyyyy"

r_number = random.randint( 1111, 9999 )              # To create unique repository name
new_repo = "my_new_repo_" + str( r_number )


# Challenge #1: Repository Creation_________________________________________________________!

driver.get( 'https://github.com/login' )
driver.find_element_by_xpath( "//input[@type='text'][contains(@id,'field')]" ).send_keys( username )
driver.find_element_by_xpath( "//input[@id='password']" ).send_keys( password )
driver.find_element_by_xpath( "//input[contains(@type,'submit')]" ).click()
driver.find_element_by_xpath( "(//span[@class='dropdown-caret'])[1]" ).click()
driver.find_element_by_xpath( "//a[@role='menuitem'][contains(.,'New repository')]" ).click()
driver.find_element_by_xpath( "//input[@autocapitalize='off'][contains(@id,'name')]" ).send_keys( new_repo )
time.sleep( 10 )
driver.find_element_by_xpath( "//button[contains(.,'Create repository')]" ).click()


# Challenge #2: Issue Creation_______________________________________________________________!
# Navigate to home page->
driver.find_element_by_xpath( "//summary[contains(@aria-label,'View profile and more')]" ).click()
time.sleep( 2 )
driver.find_element_by_xpath( "//a[contains(.,'Your repositories')]" ).click()
time.sleep( 10 )
string = "//a[contains(.,'old_string')]"
string = string.replace( "old_string", new_repo )
driver.find_element_by_xpath( string ).click()
time.sleep( 2 )
driver.find_element_by_xpath( "//span[contains(.,'Issues')]" ).click()
driver.find_element_by_xpath( "//span[contains(.,'New issue')]" ).click()
time.sleep( 2 )
driver.find_element_by_xpath( "//input[contains(@name,'issue[title]')]" ).send_keys(
    "Calculator.py not working properly" )
driver.find_element_by_xpath( "//button[@class='btn btn-primary']" ).click()
time.sleep( 2 )
driver.find_element_by_xpath( "//span[contains(.,'Issues')]" ).click()
driver.find_element_by_xpath( "//span[contains(.,'New issue')]" ).click()
driver.find_element_by_xpath( "//input[contains(@name,'issue[title]')]" ).send_keys( "System getting hanged while "
                                                                                     "running Calculator.py tool" )
driver.find_element_by_xpath( "//textarea[contains(@placeholder,'Leave a comment')]" ).send_keys( "There is an "
                                                                                                  "compatibility issue "
                                                                                                  "with Calculator.py\n "
                                                                                                  "due to that system "
                                                                                                  "getting hanged while "
                                                                                                  "running the tool. "
                                                                                                  "Related issue also "
                                                                                                  "created as "
                                                                                                  "\nCalculator.py not "
                                                                                                  "working properly." )
driver.find_element_by_xpath( "//button[@class='btn btn-primary']" ).click()
time.sleep( 2 )

# Challenge #3: Comment to an Issue_____________________________________________________________!
# Navigate to home page->
driver.find_element_by_xpath( "//summary[contains(@aria-label,'View profile and more')]" ).click()
time.sleep( 2 )
driver.find_element_by_xpath( "//a[contains(.,'Your repositories')]" ).click()
time.sleep( 10 )
driver.find_element_by_xpath( string ).click()
time.sleep( 2 )
driver.find_element_by_xpath( "//span[contains(.,'Issues')]" ).click()
driver.find_element_by_xpath( "//a[@id='issue_1_link']" ).click()
time.sleep( 2 )
driver.find_element_by_xpath( "//textarea[@id='new_comment_field']" ).send_keys(
    "In Calculator.py tool, at code line - "
    "28, there is not break statement \n "
    "because of that tool is running in "
    "infinite loop.\n :relaxed:" )
driver.find_element_by_xpath( "//button[@type='submit'][contains(.,'Comment')]" ).click()
time.sleep( 2 )

# Challenge #4: Issue mention in comments link to Issue_____________________________________________________________!
# Navigate to home page->
driver.find_element_by_xpath( "//summary[contains(@aria-label,'View profile and more')]" ).click()
time.sleep( 2 )
driver.find_element_by_xpath( "//a[contains(.,'Your repositories')]" ).click()
time.sleep( 10 )
driver.find_element_by_xpath( string ).click()
time.sleep( 2 )
driver.find_element_by_xpath( "//span[contains(.,'Issues')]" ).click()
driver.find_element_by_xpath( "//a[@id='issue_2_link']" ).click()
time.sleep( 2 )
driver.find_element_by_xpath( "//textarea[@id='new_comment_field']" ).send_keys(
    "Calculator.py tool running in infinite "
    "loop is fixed which is mentioned in "
    "the issue #1. System hanging issue "
    "also resolved." )
driver.find_element_by_xpath(
    "//button[@type='submit'][contains(.,'Comment')]" ).click()  # Create a new comment and mention any of the previous issue
time.sleep( 5 )
driver.find_element_by_xpath("//a[@class='issue-link js-issue-link'][contains(.,'#1')]" ).click()  # Navigate to the issue from the comment
time.sleep( 2 )

# Challenge #5: Delete repository_____________________________________________________________!
# Navigate to home page->
driver.find_element_by_xpath( "//summary[contains(@aria-label,'View profile and more')]" ).click()
time.sleep( 2 )
driver.find_element_by_xpath( "//a[contains(.,'Your repositories')]" ).click()
time.sleep( 10 )
driver.find_element_by_xpath( string ).click()
time.sleep( 2 )
driver.find_element_by_xpath( "//span[contains(.,'Settings')]" ).click()
time.sleep( 2 )
driver.find_element_by_xpath( "//summary[contains(.,'Delete this repository')]" ).click()
time.sleep( 10 )
confirmationName = usr + "/" + new_repo
driver.find_element_by_xpath( "//input[@aria-label='Type in the name of the repository to confirm that you want to "
                              "delete this repository.']" ).send_keys( confirmationName )

driver.find_element_by_xpath( "//button[@type='submit'][contains(.,'I understand the consequences, delete this "
                              "repository')]" ).click()

# -----------------Finished----------------------
