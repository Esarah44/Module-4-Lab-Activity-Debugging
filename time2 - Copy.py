# Program Name: time2.py
# Purpose of a program:
# User inputs current time and hours to wait.
# Then program returns the time user's waiting time ends.
                                        #typo change tiime to time

str_time = input("What time is it now?")
str_wait_time = input("What is the number of hours to wait?")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_ends = time + wait_time
print(time_when_ends)


