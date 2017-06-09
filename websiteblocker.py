import time
from datetime import datetime as dt #data time module to access current date from the system

hosts_temp="hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"  #hosts file path where list of links to be blocked is saved
redirect="127.0.0.1"                                #redirection to local host
website_list=["www.facebook.com","facebook.com"]    #list of sites to be blocked

while True: #scripts runs all the time since True is passed
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16): # compares current date and time to 9am-5pm of the same day
        print("Working Hours")
        with open(hosts_temp, 'r+') as file:    #opens hosts_temp as r+; read and write mode
            content = file.read()               #stores file content in content variable
            for websites in website_list:       #forloop for iterating through website_list
                if websites in content:         #checking if websites present in content
                    pass
                else:
                    file.write(redirect + " " + websites + "\n")

    else:
        print("Party hard")
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()          #readlines() reads content line by line
            file.seek(0)                        #puts the pointer at the start of the file. pointer at end by default.
            for line in content:                #each line in the content
                #if no website str present in the line executes the following loop
                if not any(website in line for website in website_list):   #condition: if no website in line | website name from website_list
                    file.write(line)                                       #writes each line one by one at the pointer position. ref line 24
            file.truncate()                                                #delete anything after the block of lines are written in the file containing no website names

    time.sleep(5) #5 seconds delay
