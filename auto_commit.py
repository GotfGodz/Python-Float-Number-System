import os
import datetime

# Path to the file you want to modify
file_path = 'daily_updates.txt'

# Create or update the file with the current date and time
with open(file_path, 'a') as file:
    file.write(f"Update made on: {datetime.datetime.now()}\n")

# Run git commands to commit and push
os.system("git add .")
os.system('git commit -m "Automated commit: update at {}"'.format(datetime.datetime.now()))
os.system("git push origin main")  # Change 'main' if your default branch is different
