import csv

list2 =[]
with open('sample.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader) 

# Print the 3rd row of csv file.
print("The 3rd row of csv file : ")
print(rows[3]) 


# Only the 2nd column of the csv file.
print()
print("Printing only the 2nd column of csv file :")
with open('sample.csv','r') as file:
    reader = csv.reader(file)
    for i in reader:
        print(i[2])


# First 3 lines of the csv file.
print()
print("Printing first 3 lines of csv file :")
count = 0
with open('sample.csv',"r") as file:
    reader = csv.reader(file)
    rows = list(reader)
    for i in rows:
       if(count< 3):
           print(i)
           count = count+1
       else:
            exit   