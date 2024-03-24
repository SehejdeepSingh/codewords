import os
import datetime
import json

# Load the pattern
with open("pattern-4m69bi.json", "r") as file:
    # Properly load JSON to handle formatting
    pattern = json.load(file)

# Set start date (adjust the year to fit your GitHub contribution year)
start_date = datetime.date(2024, 3, 1)

# Generate commits based on the pattern
for week, row in enumerate(pattern):
    for day, cell in enumerate(row):
        # Skip empty cells
        if cell.strip() and cell.isdigit():  
            commits = int(cell)
            for _ in range(commits):
                date = start_date + datetime.timedelta(weeks=week, days=day)
                date_str = date.strftime("%Y-%m-%d")

                # Create a commit
                with open("pattern.txt", "a") as f:
                    f.write(f"Commit on {date_str}\n")

                # Add and commit with date override (Windows syntax)
                os.system(f'git add .')
                os.system(f'set GIT_COMMITTER_DATE={date_str}T12:00:00 && git commit --date="{date_str}T12:00:00" -m "Commit on {date_str}"')

# Push the commits
os.system("git push origin main")
