# Write a python program to get all the filenames of the files and print them in an ascending order.

import os

list_dir = os.listdir('.')  #to get the list of directory content.
list_dir = [f.lower() for f in list_dir]   # Convert to lower case

print(sorted(list_dir))