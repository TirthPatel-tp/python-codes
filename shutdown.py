import os
import datetime
import time

name= input("Enter your Name:- ")
print(name)


# Asking user to get time for shutdown
shutdown_input =input("Enter date and time in YYYY-MM-DD HH:MM:SS format To shutdown the Laptop: ")  # year, month, day, hour, minute, second
shutdown_time = datetime.datetime.strptime(shutdown_input, '%Y-%m-%d %H:%M:%S')

print(shutdown_time)


# Get the current time
current_time = datetime.datetime.now()
print(current_time)


# Calculate the number of seconds until the specified shutdown time
time_difference = (shutdown_time - current_time).total_seconds()

conformation = input("Do you wish to shutdown your computer ? (yes / no): ")
   
if conformation == 'yes':
    # Wait until the shutdown time
    if time_difference > 0:
     time.sleep(time_difference)
else:
    exit()

# Shut down the computer
os.system("shutdown /s /t 1")
