from datetime import date

def days_between_dates(date1, date2):
    # Convert tuples into date objects
    d1 = date(date1[2], date1[1], date1[0])  # year, month, day
    d2 = date(date2[2], date2[1], date2[0])  # year, month, day
    
    # Calculate the difference in days
    difference = abs((d2 - d1).days)
    return difference

# Example date tuples (day, month, year)
date1 = (5, 4, 2025)  # 5th April 2025
date2 = (10, 4, 2025)  # 10th April 2025

days_difference = days_between_dates(date1, date2)

print("Number of days between the two dates:", days_difference)