""" @author: Adam, @date 6/16/2019 """

import time

def is_leap(year):
    """Check if year is a leap year."""
    if (year % 100 == 0):
        return year % 400 == 0
    else:
        return year % 4 == 0
    
def get_first_month_days(month_to_days):
    """Return list of first month days of the year given a dictionary of
    (key, value) = (month, number of days in month) pairs. """
    first_month_days = []
    day_count = 1
    for days in month_to_days.values():
        first_month_days.append(day_count)
        day_count += days
    return first_month_days
        
#%% Find all first month days of the year and check if they are Sunday.

start = time.time()

# Dictionaries to determine first month days of the year.
month_to_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30,
                 10:31, 11:30, 12:31}
month_to_days_leap = month_to_days.copy()
month_to_days_leap[2] = 29

n_sun = 0
year_start_day = 2  # Jan 1, 1901 was a Tuesday. M, Tu, ..., Su = 1, 2, ..., 7.
for year in range(1901, 2001):
    # Compute first month days, checking for leap years.
    if is_leap(year):
        first_month_days = get_first_month_days(month_to_days_leap)
        year_end_day = (year_start_day - 1 + 366) % 7
    else:
        first_month_days = get_first_month_days(month_to_days)
        year_end_day = (year_start_day - 1 + 365) % 7

    # Count number of Sundays and update start day for the next year.
    is_sunday = [(year_start_day - 1 + day) % 7 == 0
                    for day in first_month_days]
    n_sun += sum(is_sunday)
    year_start_day = (year_end_day + 1) % 7
    
print(n_sun)

print(time.time() - start)

#%%
""" Potential Improvements:

    Extensions / Remarks:
1)  This could be estimated by counting the number of months and dividing by
    the number of days, which assumes first month days are uniformly
    distributed among days: 100 * 12 / 7 = 171.42...
2)  This can be easily extended to check any day by modifying line 44
    to == 1, 2, ..., 6.
"""




