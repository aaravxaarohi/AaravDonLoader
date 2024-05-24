from urllib import response
import mechanize
import os
import datetime
import sys
from time import sleep
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')]
browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
        sleep(0.03)

logo =  """\033[1;35;40m    
 \033[1;35;40m      
 $$$$$   /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$    /$$      
 /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$| $$   | $$      
| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$   | $$      
| $$$$$$$$| $$$$$$$$| $$$$$$$$| $$$$$$$/| $$$$$$$$|  $$ / $$/      
| $$__  $$| $$__  $$| $$__  $$| $$__  $$| $$__  $$ \  $$ $$/       
| $$  | $$| $$  | $$| $$  | $$| $$  \ $$| $$  | $$  \  $$$/        
| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$   \  $/         
|__/  |__/|__/  |__/|__/  |__/|__/  |__/|__/  |__/    \_/          
                                                                   
                                                                   
                                                            
                                        
                                        
                                                                                 
                                        
                                        
                                                                                                                  
\033[1;34;40m-----------------------------------------------
\033[1;34;40mM9D3 BY  : Aarav Don
\033[1;34;40mFacebook : https://www.facebook.com/profile.php?id=aaravshr8ivastav
\033[1;34;40mWhatsapp: +918809497526
\033[1;34;40m-----------------------------------------------"""

def menu():
	os.system('clear')
	print(logo)
	print('[1] Random Uid Crack')
	print('[2] Contact To Owner')
	print('[0] Exit')
	print(47*"-")
	opt = input('[?] Choose : ')
	if opt =='1':
		md()
	elif opt =='2':
		Contact()
	elif opt =='0':
		exit()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		menu()

def login():
    browser.open(url)
    browser.select_form(nr = 0)
    browser.form['email'] = USERNAME
    browser.form['pass'] = PASSWORD
    r = browser.submit()
    f = open("login.html", "wb")
    f.write(r.read())
    f.close()
    browser.select_form(nr = 0)
    print("\033[1m\033[36m", end = "")
    print(47*'\033[1;35;40m-')
    sp("\033[1;37;1m[?] Enter the 2 factor code by google authenticator\n")
    print(47*'\033[1;37;1m-')
    apr = str(input('\033[1;37;1m[?] Enter Code : '))
    try:
        browser.form['approvals_code'] = apr
    except mechanize._form_controls.ControlNotFoundError:
        print("Wrong password or some shit, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    browser.select_form(nr = 0)
    try:
        browser.form['name_action_selected'] = ['save_device']
    except mechanize._form_controls.ControlNotFoundError:
        print("Some shit gone down, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    f = open("full_login_" + str(USERNAME) + ".html", "wb")
    f.write(r.read())
    f.close()

def findtextchat(curl):
    r = browser.open(curl)
    x = browser.title()
    if x == "Review recent login":
        print("\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.")
        exit(1)
    if x == "Login approval needed":
        print("\nYour account is stuck on verification\nPlease do it and then re run the program.")
        exit(1)
    if x == "Epsilon":
        print("\nYour account got locked, recover it kindly and re run the script.")
        exit(1)

def sendtextconvo(comment):
    try:
        browser.select_form(nr = 1)
    except mechanize._mechanize.FormNotFoundError:
        print("Some error occured while finding text area, please check your account")
        exit(1)
    try:
        browser.form['body'] = comment
    except mechanize._form_controls.ControlNotFoundError:
        print("Some error occured while filling text, please check your account")
        exit(1)
    r = browser.submit()
    e = datetime.datetime.now()
    print("\033[1;35;40m",end = "")
    print (e.strftime(" Ha mƏri Jawn ChaLa Gya tƏra MsG  :: Date - %d/%m/%Y  Time - %I:%M:%S %p"))
    print(">> SoJa Bhai/Jawn Main Dəkh LunGa Əb  :: ", line, "\n")

print("\033[1;33;40m", end = "")
os.system('clear')
print(logo)
sp("\033[1m\033[36m[ ] mƏri Jawn ApnƏ Fb İD Ka NumbƏr Ya Email Likh \n")
print(47*'\033[1;35;40m-')
USERNAME = str(input('[ ] mƏri Jawn NumbƏr Ya EmaiL LikH  : '))
print("\033[1;33;40m", end = "")
print(47*'\033[1;35;40m-')
sp("\033[1m\033[36m[ ] PassworD Bhi Likh Də mƏri Jaw'n\n")
print(47*'\033[1;35;40m-')
PASSWORD = str(input('[] Apni İD Ka PassworD Likh Də Jawn : '))
login()
print("\033[1;34;40m", end = "")
print(47*'\033[1;35;40m-')
sp("\033[1m\033[36m[?] Group Chat/inbox Link\n")
print(47*'\033[1;35;40m-')
cid = str(input('\033[1;37;1m[?]Jisko Thokna Hai Uska id ka Link Likh mƏri Jawn : '))
curl = 'https://m.facebook.com/messages/t/' + str(cid)

print("\033[1;34;40m", end = "")
print(47*'\033[1;35;40m-')
sp("\033[1m\033[36m[?] Notepad GaLi File Name Likh Jawn \n")
print(47*'\033[1;35;40m-')
np = str(input('\033[1;37;1m[?]  GaLi File Name Likh Jawn  : '))
f = open(np, 'r')
lines = f.readlines()
f.close()
print("\033[1;33;40m", end = "")
print(47*'\033[1;35;40m-')
sp("\033[1m\033[36m[?] Jitna Dər mƏ Msg Bhejna Hai Utna Seconds Likh mƏri Jawn\n")
print(47*'\033[1;35;40m-')
t = int(input('\033[1;37;1m[?] Seconds Likh Jawnu : '))

os.system('clear')
print(logo)

count = 0
while True:
    for line in lines:
        if len(line) > 3:
            if count != 0:
                sleep(t)
            findtextchat(curl)
            sendtextconvo(line)
            count += 1
            if count % 10 == 0:
                sleep(1)
                clear()
                print("\033[0;37;41m\n")
               
                
