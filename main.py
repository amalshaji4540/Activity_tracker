#!/usr/bin/env python3
import csv
from datetime import date
import time
from datetime import datetime 

csvfile = open('tracker.csv', 'a',newline='\n')
c = csv.writer(csvfile)
data=[]
start=input("You are going to enter an activity, Do you want to continue ?[Y/n]")
if (start=="Y" or start=="y"):
    today_date=date.today()
    data.append(today_date)
    activity=input("Enter the activity you are going to do \n")
    data.append(activity)
    start_time=time.strftime("%H:%M:%S", time.localtime())
    a=input("Press enter after completing the work")
    end_time=time.strftime("%H:%M:%S", time.localtime())
    start = datetime.strptime(start_time, "%H:%M:%S") 
    end = datetime.strptime(end_time, "%H:%M:%S") 
    difference = end - start 
    data.append(start_time)
    data.append(end_time)
    data.append(difference)
    seconds = difference.total_seconds() 
    minutes = round(seconds / 60,2)
    data.append(minutes)
    print(f'You had worked for \n{minutes} minutes')
    # write a column headings row - do this only once -
    c.writerow(data)
    # save and close the file
    csvfile.close()
else:
    csvfile.close() 

