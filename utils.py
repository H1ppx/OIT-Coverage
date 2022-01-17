from cgi import test
from datetime import datetime
from enum import Enum
import pandas as pd

class Level(Enum):
    Lv1 = 3 # Level 1 
    Lv2 = 4 # Level 2
    Lv2AE = 5 # Level 2 Apps/Email

def checkFree(file, level, date, startTime, endTime):
    availablePeople= []
    df = pd.read_excel(file)
    for x in range(len(df.columns)):
        if(df.iat[level,x] == True): # Check if level is true on xlsx for current person
                if(df.iat[date.weekday()+7,x]<=startTime and df.iat[date.weekday()+8,x]>=endTime): # Check if shifttime is past start time and shift time ends before endtime on current person
                    availablePeople.append(df.iat[1,x]) # Add netid to list
    return availablePeople

                

            



