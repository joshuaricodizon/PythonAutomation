from modules import *

executable_path = "/Users/joshuadizon/desktop/automation-project-yuba/chromedriver"
email = raw_input('Please enter your email to log in: ')
password= raw_input('Please enter your password: ')




chrome_options = Options()
# chrome_options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=executable_path)
wait = WebDriverWait(driver, 10)

# Visit Google's sign in page

driver.get("https://app.schoology.com/login")

try:
    # Email Entry
    print("- Entering email...")
    wait.until(EC.element_to_be_clickable((By.ID, "edit-mail"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, 'edit-mail'))).send_keys(email)    
except WebDriverException:
	print("Test Failed!")


try:
    # Password Entry
    print("- Entering password...")
    wait.until(EC.element_to_be_clickable((By.ID, "edit-pass"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, 'edit-pass'))).send_keys(password)    
except WebDriverException:
	print("Test Failed!")

try:
	#Logging in
	print("- Logging in...")
	wait.until(EC.element_to_be_clickable((By.ID, "edit-submit"))).click()
except WebDriverException:
	print("Test Failed!")

try:
	#Locating CIS301
	print("- Locating CIS301...")
	wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div/ul/li[1]/div/div/div[2]/span[1]/div/a[2]"))).click()
except WebDriverException:
	print("Test Failed!")

try:
	#Opening syllabus
	print("- Opening syllabus...")
	wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div/div[2]/form/div/table/tbody/tr[1]/td/div/div/div[2]/div/div/span/a"))).click()
except WebDriverException:
	print("Test Failed!")

try:
	#Downloading syllabus
	print("- Downloading syllabus...")
	wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div[2]/div[2]/div/div/span[2]/a[1]"))).click()
except WebDriverException:
	print("Test Failed!")

try:
	#Initiate Logging Out
	print("- Logging out...")
	wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/header/nav/ul[2]/li[6]/div/button"))).click()
except WebDriverException:
	print("Test Failed!")



try:
	#Logging Out
	print("- Laoding...")
	wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/header/nav/ul[2]/li[6]/div/ul/li[6]/a"))).click()
except WebDriverException:
	print("Test Failed!")







finally:
	print("Automation successful!")
	
