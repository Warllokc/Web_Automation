from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import webbrowser, os
from PIL import Image

# OPEN THE BROWSER/(MAKE SURE 'chromedriver' IS UPDATED TO THE VERSION OF YOUR CHROME)
browser = webdriver.Chrome('C:\\Users\\apetricenco\\Downloads\\chromedriver')
browser.get('https://www.amazon.com/')
browser.maximize_window()

# TYPE ON SEARCH BAR WHAT WE WANT TO SEARCH
searchbar = browser.find_element_by_id('twotabsearchtextbox')
searchbar.send_keys('umbrellas')
searchbar.send_keys(Keys.ENTER)
time.sleep(2)

# FINDING ELEMENTS Using XPATH
browser.find_element_by_xpath(""" //*[@id="p_72/2661618011"] """).click()
endresult = browser.find_elements_by_xpath("""//*[@id="twotabsearchtextbox"]""")
time.sleep(3)

# SAVE A SCREENSHOT
os.chdir("C:\\Users\\apetricenco\\Desktop")
browser.save_screenshot('Result.png')
im = Image.open('Result.png')
im.show()

webbrowser.open(os.path.realpath('C:\\Users\\apetricenco\\Desktop'))
print('Saving SUCCESS!!!!')


# SENDING EMAIL WITH SAVED web page
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# IF USING GMAIL.COM, MAKE SURE 'Less secure app access' IS ON
# OTHERWISE WILL RECEIVE AN ALERT

# DEFINING EMAILS 'FROM' / 'TO'
mymail = '****@gmail.com'           # FROM email addres
emailsent = '*****@yahoo.com'       # TO email addres
subject = 'Python!'					# Adding a Subject to the email

# COMPLETE TEXT FIELDS AND MESSAGE IT SELF
msg = MIMEMultipart()
msg['From'] = mymail
msg['To'] = emailsent
msg['Subject'] = subject

# Message to send
body = 'Hi this message is sent from Python script!!!'
msg.attach(MIMEText(body, 'plain'))

# File to attach
filename = 'Result.png'

os.chdir('C:\\Users\\apetricenco\\Desktop')
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename = "+filename)
msg.attach(part)
text = msg.as_string()

# Connecting to server
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(mymail, '*********')       # personal credentials / password
server.sendmail(mymail, emailsent, text)
server.quit()

print ('Sending SUCCESS!!!!!!!!!')

# Enjoy coding!!!
