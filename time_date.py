#3. Write a Python program to display the current date and time.
#Sample Output :
#Current date and time :
#2014-07-05 14:34:14

# Answer


import datetime

current = datetime.datetime.now()

print("The current time is ")
print(current.strftime("%Y-%m-%d %H:%M:%S"))