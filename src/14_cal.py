"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

#capture command line inputs in a variable
#print the calendar
#handle different numbers of command line arguments

#set the current date w/datetime.now(), and the month, year
date = datetime.now()
month = date.month
year = date.year
#can also write month,year = date.month, date.year

#set month to new_month, make that global so it doesn't just hang out locally
def change_month(new_month):
    global month
    month = new_month

#set year to new year, set it to global
def change_year(new_year):
    global year
    year = new_year

#if/else to change month and year (lots of stackoverflow here--need to work through this logic more thoroughly)
if (len(sys.argv) == 2):
    change_month(int(sys.argv[1]))
elif(len(sys.argv) == 3):
    change_month(int(sys.argv[1]))
    change_year(int(sys.argv[2]))


print(calendar.month(year, month))

#How Tim did it
# today = datetime.today()
# month, year = today.month, today.year
# cal = calendar.TextCalendar(firstweekday=6)

# # print(sys.argv)
# if len(sys.argv) == 1:
#   calendar.prmonth(today.year, today.month)

# elif len(sys.argv) == 2:
#   calendar.prmonth(today.year, int(sys.argv[1]))

# elif len(sys.argv) == 3:
#   calendar.prmonth(int(sys.argv[2]), int(sys.argv[1]))

# else:
#   print("usage: filename month year")
#   sys.exit(1)