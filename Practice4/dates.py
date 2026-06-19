from datetime import datetime, timedelta

# Exercise 1
# Subtract five days

today = datetime.now()

five_days_ago = today - timedelta(days=5)

print("Current date:", today)
print("5 days ago:", five_days_ago)


# Exercise 2
# Yesterday, Today, Tomorrow

today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())


# Exercise 3
# Drop microseconds

current_time = datetime.now()

without_microseconds = current_time.replace(microsecond=0)

print("Original:", current_time)
print("Without microseconds:", without_microseconds)


# Exercise 4
# Difference in seconds

date1 = datetime(2025, 1, 1, 12, 0, 0)
date2 = datetime(2025, 1, 2, 12, 0, 0)

difference = date2 - date1

print("Difference in seconds:", difference.total_seconds())
