"""
Lesson 11: Math & Date Time Calendar
This lesson covers Python math operations and datetime/calendar handling with examples.
"""

import math
import datetime
import calendar
from datetime import timedelta

# Example 1: Basic Math Operations
def basic_math_operations():
    """Demonstrate basic math operations"""
    return {
        "pi": math.pi,
        "e": math.e,
        "sqrt(16)": math.sqrt(16),
        "pow(2, 3)": math.pow(2, 3),
        "abs(-5)": abs(-5),
        "round(3.7)": round(3.7),
        "floor(3.7)": math.floor(3.7),
        "ceil(3.7)": math.ceil(3.7)
    }

# Example 2: Trigonometric Functions
def trigonometric_functions():
    """Demonstrate trigonometric functions"""
    angle = math.pi / 4  # 45 degrees
    return {
        "sin(45°)": math.sin(angle),
        "cos(45°)": math.cos(angle),
        "tan(45°)": math.tan(angle),
        "degrees(π/4)": math.degrees(angle),
        "radians(45)": math.radians(45)
    }

# Example 3: Working with Dates
def date_operations():
    """Demonstrate date operations"""
    today = datetime.date.today()
    return {
        "today": today,
        "year": today.year,
        "month": today.month,
        "day": today.day,
        "weekday": today.weekday(),
        "isoweekday": today.isoweekday()
    }

# Example 4: Working with Time
def time_operations():
    """Demonstrate time operations"""
    current_time = datetime.datetime.now().time()
    return {
        "current_time": current_time,
        "hour": current_time.hour,
        "minute": current_time.minute,
        "second": current_time.second,
        "microsecond": current_time.microsecond
    }

# Example 5: Date Arithmetic
def date_arithmetic():
    """Demonstrate date arithmetic"""
    today = datetime.date.today()
    return {
        "today": today,
        "tomorrow": today + timedelta(days=1),
        "yesterday": today - timedelta(days=1),
        "next_week": today + timedelta(weeks=1),
        "days_between": (today + timedelta(days=7) - today).days
    }

# Example 6: Calendar Operations
def calendar_operations():
    """Demonstrate calendar operations"""
    cal = calendar.TextCalendar()
    return {
        "current_month": cal.formatmonth(datetime.date.today().year, datetime.date.today().month),
        "is_leap_year": calendar.isleap(datetime.date.today().year),
        "month_range": calendar.monthrange(datetime.date.today().year, datetime.date.today().month),
        "month_name": calendar.month_name[datetime.date.today().month],
        "day_name": calendar.day_name[datetime.date.today().weekday()]
    }

# Example 7: Date Formatting
def date_formatting():
    """Demonstrate date formatting"""
    now = datetime.datetime.now()
    return {
        "strftime_default": now.strftime("%Y-%m-%d %H:%M:%S"),
        "strftime_custom": now.strftime("%d/%m/%Y %I:%M %p"),
        "iso_format": now.isoformat(),
        "ctime": now.ctime()
    }

# Testing the functions
if __name__ == "__main__":
    # Test Example 1
    print("Example 1 - Basic Math Operations:")
    for key, value in basic_math_operations().items():
        print(f"{key}: {value}")
    
    # Test Example 2
    print("\nExample 2 - Trigonometric Functions:")
    for key, value in trigonometric_functions().items():
        print(f"{key}: {value}")
    
    # Test Example 3
    print("\nExample 3 - Date Operations:")
    for key, value in date_operations().items():
        print(f"{key}: {value}")
    
    # Test Example 4
    print("\nExample 4 - Time Operations:")
    for key, value in time_operations().items():
        print(f"{key}: {value}")
    
    # Test Example 5
    print("\nExample 5 - Date Arithmetic:")
    for key, value in date_arithmetic().items():
        print(f"{key}: {value}")
    
    # Test Example 6
    print("\nExample 6 - Calendar Operations:")
    for key, value in calendar_operations().items():
        print(f"{key}: {value}")
    
    # Test Example 7
    print("\nExample 7 - Date Formatting:")
    for key, value in date_formatting().items():
        print(f"{key}: {value}") 