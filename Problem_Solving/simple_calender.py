import calendar

# Create a plain text calendar
cal = calendar.TextCalendar(firstweekday=0)
year_calendar = cal.formatyear(2025)

print(year_calendar)
