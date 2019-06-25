import time
from datetime import datetime as dt

#directory location for hosts file
hosts_path = 'etc/hosts'
redirect = "127.0.0.1"

#list of websites which you want to block
website_list = ["facebook.com", "www.facebook.com"]

while(1):
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() <  dt(dt.now().year, dt.now().month, dt.now().day, 18):
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)

#this file has to be set in a cron in Linux and Mac based systems. Once set in a cron, It will automatically render the host files and toggle the website blocklisting.
