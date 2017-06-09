import time

host_path=r"C:\Windows\System32\drivers\etc\hosts" #hosts file path where list of links to be blocked is saved
redirect="127.0.0.1" #redirection to local host
website_list=["www.facebook.com","facebook.com"] #list of sites to be blocked

while True:
    print(1)
    time.sleep(5) #5 seconds delay
