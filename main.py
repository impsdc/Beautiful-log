import os
import re 
import subprocess
from pathlib import Path

subprocess.call("pm2 stop live", shell="True")
accessLog = Path('access.log')
filteredLog = Path('/root/filteredLog')

if accessLog.exists(): 
    os.remove(accessLog)

#If log file is located in a another server
subprocess.call("rsync log file", shell=True)

logs = open(accessLog, "r")

for each_line in logs:
    filter = each_line.split(" ")
    
    if filter[4] == 'GET' and "wp-" not in filter[5] and "image_captcha" not in filter[5] and "robots.txt" not in filter[5] and "sitemap" not in filter[5] and "xmlrpc" not in filter[5]:
        print( "ip : " + filter[1] + " - page : " + filter[5] + ' - date : ' + filter[2].replace("[", "") + "\n", file=open(filteredLog, "a"))


subprocess.call('pm2 start live', shell=True)
