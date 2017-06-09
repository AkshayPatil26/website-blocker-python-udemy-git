import time
from datetime import datetime as dt

host_path=r"C:\Windows\System32\drivers\etc\hosts" #hosts file path where list of links to be blocked is saved
redirect="127.0.0.1" #redirection to local host
website_list=["www.facebook.com","facebook.com"] #list of sites to be blocked

while True: #scripts runs all the time since True is passed
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working Hours")
    else:
        print("Party hard")

    time.sleep(5) #5 seconds delay
