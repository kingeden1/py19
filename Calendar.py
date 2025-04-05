import calendar 
yy= 2025
mm=3
print(calendar.month(yy,mm))

import calendar
# Get all month names
months = list(calendar.month_name)
months = months [1:]
# Print the month names
for month in months:
    print(month)