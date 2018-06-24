import datetime

months_length=[0,31,28,31,30,31,30,31,31,30,31,30,31] ##the 1st month is on the 1st position

current_time = datetime.datetime.now()

##nobody knows the second they were born
##if you were born at 12:00:59, when the time becomes 12:01:00 the script thinks that you already have lived for 60 seconds
##although you have lived for only one second, so in the worst case the error consists of 59 seconds
##the error could become 0 in the event that a user would know the exact second in which he/she was born
##from this point just taking into account a birth_second variable and a current_second variable, should provide an accurate answer

current_minute = current_time.minute
current_hour = current_time.hour
current_day = current_time.day
current_month = current_time.month
current_year = current_time.year

print("Enter your birthday:")

print("Year:" ,end = '') 
birth_year = int(input())
assert(birth_year>=1 and birth_year<=current_year), "Please enter a valid value"

print("Month:",end = '')
birth_month = int(input())
assert(birth_month>=1 and birth_month<=12), "Please enter a valid value"


print("Day:",end = '')
birth_day = int(input())
assert(birth_day>=1 and birth_day<=31), "Please enter a valid value"


print("Hour:",end = '')
birth_hour = int(input())
assert(birth_hour>=0 and birth_hour<=23), "Please enter a valid value"


print("Minute:",end = '')
birth_minute = int(input())
assert(birth_minute>=0 and birth_minute<=59), "Please enter a valid value"



## Leap years lived by the user
leap_years = 0
for i in range(birth_year+1,current_year):
    if i%4==0:
        leap_years+=1

if birth_year%4==0 and birth_month<=2: ##people born on 29th of February?
    leap_years+=1
if current_year%4==0 and current_month>2:
    leap_years+=1

## Whole years lived by the user
if current_month>birth_month:
    years = current_year - birth_year
elif current_month<birth_month:
    years = current_year - birth_year - 1
elif current_month == birth_month and current_day>birth_day:
    years = current_year - birth_year
elif current_month == birth_month and current_day<birth_day:
    years = current_year - birth_year-1
elif current_month == birth_month and current_day==birth_day and current_hour>birth_hour:
    years = current_year - birth_year
elif current_month == birth_month and current_day==birth_day and current_hour<birth_hour:
    years = current_year - birth_year-1
elif current_month == birth_month and current_day==birth_day and current_hour==birth_hour and current_minute>=birth_minute:
    years = current_year - birth_year
else: years = current_year - birth_year-1

    

## Months lived in addition to the years lived
if current_month<birth_month and current_day>birth_day:
    months = 12 - abs(current_month - birth_month)
elif current_month<birth_month and current_day<birth_day:
    months = 12 - abs(current_month - birth_month)-1
elif current_month<birth_month and current_day==birth_day and current_hour>birth_hour:
    months = 12 - abs(current_month - birth_month)
elif current_month<birth_month and current_day==birth_day and current_hour<birth_hour:
    months = 12 - abs(current_month - birth_month)-1
elif current_month<birth_month and current_day==birth_day and current_hour==birth_hour and current_minute>=birth_minute:
    months = 12 - abs(current_month - birth_month)
elif current_month<birth_month and current_day==birth_day and current_hour==birth_hour and current_minute<birth_minute:
    months = 12 - abs(current_month - birth_month)-1

elif current_month>birth_month and current_day>birth_day:
    months = current_month-birth_month
elif current_month>birth_month and current_day<birth_day:
    months = current_month-birth_month-1
elif current_month>birth_month and current_day==birth_day and current_hour>birth_hour:
    months = current_month-birth_month
elif current_month>birth_month and current_day==birth_day and current_hour<birth_hour:
    months = current_month-birth_month-1
elif current_month>birth_month and current_day==birth_day and current_hour==birth_hour and current_minute>=birth_minute:
    months = current_month-birth_month
elif current_month>birth_month and current_day==birth_day and current_hour==birth_hour and current_minute<birth_minute:
    months = current_month-birth_month-1

elif current_month==birth_month and current_day>birth_day:
    months = 0
elif current_month==birth_month and current_day<birth_day:
    months = 11
elif current_month==birth_month and current_day==birth_day and current_hour>birth_hour:
    months = 0
elif current_month==birth_month and current_day==birth_day and current_hour<birth_hour:
    months = 11
elif current_month==birth_month and current_day==birth_day and current_hour==birth_hour and current_minute>=birth_minute:
    months = 0
elif current_month==birth_month and current_day==birth_day and current_hour==birth_hour and current_minute<birth_minute:
    months = 11


## Days lived that do not form a whole month yet
if current_hour > birth_hour :
    if current_day<birth_day:
        days = months_length[current_month-1]- birth_day + current_day
    elif current_day>birth_day:
        days = current_day-birth_day
    elif current_day == birth_day:
        days=0
        
elif current_hour < birth_hour:
    if current_day<birth_day:
        days = months_length[current_month-1]- birth_day + current_day-1
    elif current_day>birth_day:
        days = current_day-birth_day-1
    elif current_day == birth_day:
        days=0
        
elif current_hour == birth_hour and current_minute>=birth_minute:
    if current_day<birth_day:
        days = months_length[current_month-1]- birth_day + current_day
    elif current_day>birth_day:
        days = current_day-birth_day
    elif current_day == birth_day:
        days=0
elif current_hour == birth_hour and current_minute<birth_minute:
    if current_day<birth_day:
        days = months_length[current_month-1]- birth_day + current_day-1
    elif current_day>birth_day:
        days = current_day-birth_day-1
    elif current_day == birth_day:
        days=months_length[current_month-1]- birth_day + current_day - 1

## Hours lived that do not form a whole day yet
if current_minute >= birth_minute :
    if current_hour>birth_hour:
        hours = current_hour - birth_hour
    elif current_hour<birth_hour:
        hours = 24 - birth_hour +current_hour
    elif current_hour==birth_hour:
        hours=0
elif current_minute < birth_minute and current_hour>birth_hour:
    hours = current_hour - birth_hour-1
elif current_minute < birth_minute and current_hour<birth_hour:
    if current_hour == 0:
        hours = 24 - birth_hour-1
    else:hours = 24 - birth_hour +current_hour
elif current_minute < birth_minute and current_hour==birth_hour:
    hours = 23

## Minutes lived that do not form a whole hour yet
if current_minute<birth_minute:
    minutes = 60 - abs(current_minute-birth_minute)
elif current_minute>birth_minute:
    minutes = current_minute-birth_minute
else: minutes = 0

print("{} Years".format(years), "{} Months".format(months), "{} Days".format(days), "{} Hours ".format(hours), "{} Minutes".format(minutes))


months_to_days = 0
i = birth_month
reverse_counter = months
while reverse_counter != 0:
    months_to_days+=months_length[i]
    if i!=12:
        i+=1
    elif i==12:
        i=1
    reverse_counter -= 1

years_to_sec = (years*365 + leap_years)*24*60*60
months_to_sec = months_to_days*24*60*60
days_to_sec = days*24*60*60
hours_to_sec = hours*60*60
minutes_to_sec= minutes*60

total_seconds = years_to_sec + months_to_sec + days_to_sec + hours_to_sec + minutes_to_sec

print("{} Total Seconds".format(total_seconds))
