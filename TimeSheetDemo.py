from modules import *

executable_path = "/Users/joshuadizon/desktop/automation-project-yuba/chromedriver"
link = raw_input('Please enter your timesheet link: ')

chrome_options = Options()
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=executable_path)
driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.get('https://yearup.tfaforms.net/forms/view/261392?tfa_97=0033800002xB9HB&tfa_99=a0j1T00000ISQJ5')

#PAGE 1
#Monday
print('Completing Monday')
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_9'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1812'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_8'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1053'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_2165'))).click()
#Tuesday
print('Completing Tuesday')
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_388'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1788'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1150'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1151'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_2130'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_2171'))).click()
#Wednesday
print('Completing Wednesday')
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_442'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1883'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1248'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1709'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_2136'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_2177'))).click()
#Thursday
print('Completing Thursday')
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_496'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1932'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1346'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1348'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_2142'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_2183'))).click()
#Friday
print('Completing Friday')
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_562'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1976'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1444'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_1445'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_2148'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_2189'))).click()
#Internship Seminar
user_answer = raw_input('Did you attend internship seminar this week? (yes or no): ')
time.sleep(int(5))

if user_answer  == 'yes':
	wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/form/div[1]/div[1]/div[6]/div/span/span[2]/input'))).click()
else:
	wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/form/div[1]/div[1]/div[6]/div/span/span[1]/input'))).click()
#Intern Comments
intern_bool = raw_input('Do you have any comments for this week? (yes or no): ')
if intern_bool == 'yes':
	intern_comment = raw_input('Please type out any of your comments: ')
	wait.until(EC.visibility_of_element_located((By.ID, 'tfa_90'))).send_keys(intern_comment)
	wait.until(EC.element_to_be_clickable((By.ID, 'wfPageNextId2'))).click()
	print('You will be redirected to the next page.')
elif intern_bool == 'no':
	print('You will be redirected to the next page.')
	wait.until(EC.element_to_be_clickable((By.ID, 'wfPageNextId2'))).click()
else:
	print('You did not choose an option. Driver will close.')
	driver.quit()

#Page 2
#Questions
print('Please answer the follwing questions: ')
question1 = raw_input('What was your biggest achievement this week? ')
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_271'))).click()
wait.until(EC.visibility_of_element_located((By.ID, 'tfa_271'))).send_keys(question1)

question2 = raw_input('What work related challenges are you currently facing?  How do you plan to overcome them? ')
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_272'))).click()
wait.until(EC.visibility_of_element_located((By.ID, 'tfa_272'))).send_keys(question2)

question3 = raw_input(' How do you plan to continue to grow your skills in your current role?  Identify one goal for yourself on your internship next week. ')
wait.until(EC.element_to_be_clickable((By.ID, 'tfa_273'))).click()
wait.until(EC.visibility_of_element_located((By.ID, 'tfa_273'))).send_keys(question3)

# Custom Questions
print('This next portion consists of questions of your choice. Please complete this portion of the timesheet manually, the automation for this portion is still being worked on.')


# Last Question
intern_bool_2 = raw_input('Do you feel that you would benefit from extra support from Year Up this week? (yes or no): ')
if intern_bool_2 == 'yes':
	wait.until(EC.element_to_be_clickable((By.ID, ''))).click()
else:
	wait.until(EC.element_to_be_clickable((By.ID, ''))).click()
	


# Hello



