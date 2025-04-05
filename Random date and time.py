import random
import datetime
# Define the start and end dates
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2025, 12, 31)
# Generate a random number of days between the range
random_days = random.randint(0, (end_date - start_date).days)
# Get the random date
random_days = start_date
# Print the random date
print("Random Date: ", random_days)