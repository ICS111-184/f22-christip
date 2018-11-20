# -*- coding: utf-8 -*-
"""
ICS 111 Intro to Computer Science I
GICP 7.1 Exceptions and Assertions
friendsbdays.py
Christi Palacat
November 19, 2018
"""

import datetime
# Created a blank dictionary
listed={}

#Function to write dictionary into a text file
def write(): 
#Writing a text document with the name and birthday
    nameHandle = open('friendsbdays.txt', 'w')
    nameHandle.write(str(listed)) #writes out the key-value pairs in the dictionary
    nameHandle.close()
    return
#While loop that will continue to ask for a name and birthday, if not in the dictionary
while True:
    name= input('Please enter a name: ')
#Tried doing if name=='write' or 'write', but didn't work, so it's separated.  If the name is 'write' or 'write', 
#Write the dictionary to a json file and break the loop.
    if name == 'Write':
        write()
        print('Dictionary written to friendsbdays.json')
        break
    if name == 'write':
        write()
        print('Dictionary written to friendsbdays.json')
        break
# If statement to see if name is already in the dictionary.  If it's not already inputted, ask for birthdate and create new entry.
    if name not in listed:
        try:
            strdate = input('Please enter {}\'s birthdate: ' .format(name)) 
            dtbday = datetime.datetime.strptime(strdate, "%m-%d-%Y").date()
            listed[name] = dtbday
        except:
            print('ERROR: There is a problem with that date !!! ')
            strdate = input('Please enter {}\'s birthdate: ' .format(name))
            dtbday = datetime.datetime.strptime(strdate, "%m-%d-%Y").date()
            listed[name] = dtbday
#If the name is already inputted, retrieve the birthdate stored in the dictionary.
    else:
        print(name,'\'s birthday is ', listed[name],sep='')
