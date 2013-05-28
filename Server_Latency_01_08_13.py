###############################################
## Arielle Simmons                           ##
## Planner/GIS Specialist                    ##
## Pioneer Valley Planning Commission        ##
## Date created: January 08 2012             ##
###############################################

## This script runs ping (DOS external command)
## and time
## can set to specific IP

import time
import subprocess

f = open('pinglog.txt', 'a')
while True:
    print(time.asctime(time.localtime()))
    f.write(time.asctime(time.localtime()))
    try:
## need to insert server IP at the end on '...-w 15000 <server IP>'
        out = subprocess.check_output('ping -n 1 -w 15000 ')
        print(out)
        f.write(out)
    except:
        f.write ("PingError: ") 
        print ("PingError")
    time.sleep(1)
