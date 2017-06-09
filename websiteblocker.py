import time
from datetime import datetime as dt #data time module to access current date from the system

hosts_temp="hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"  #hosts file path where list of links to be blocked is saved
redirect="127.0.0.1"                                #redirection to local host
website_list=["www.facebook.com","facebook.com"]    #list of sites to be blocked

while True: #scripts runs all the time since True is passed
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17): # compares current date and time to 9am-5pm of the same day
        #print("Working Hours")
        with open(hosts_temp, 'r+') as file:    #opens hosts_temp as r+; read and write mode
            content = file.read()               #stores file content in content variable
            for websites in website_list:       #forloop for iterating through website_list
                if websites in content:         #checking if websites present in content
                    pass
                else:
                    file.write(redirect + " " + websites + "\n")

    else:
        print("Party hard")
        time.sleep(5) #5 seconds delay
