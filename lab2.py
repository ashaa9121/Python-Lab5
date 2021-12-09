#In this filename, 01022017.txt, the first 01 represents the date, 02 represents the month ( feb ) and 2017 represents the year.
#Write a python program to get all the filenames of the files and print them as
#Jan - 01012017.txt
#Feb - 01012017.txt
#Mar - 01032017.txt etc..

import os
import os.path

list_dir = os.listdir('.') 
for i in list_dir:
    s = str(i)
    #print(s)
    t = s[2]+s[3] # to get 2nd and 3rd characters..
    if(t == '01'):
        print("Jan - {}".format(i)) 
    elif(t == '02'):
        print("Feb - {}".format(i))  
    elif(t == '03'):
        print("Mar - {}".format(i))
    elif(t == '04'):
        print("Apr - {}".format(i))  
    else:
        exit        
  


