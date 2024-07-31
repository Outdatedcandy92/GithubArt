import csv
import subprocess
from datetime import datetime, timedelta
import subprocess

def read_csv(file_path):
    pixel_values = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pixel_values.append([int(value) for value in row])
    return pixel_values

def create_commits(pixel_values, year):
    start_date = datetime(year, 1, 1) - timedelta(days=datetime(year, 1, 1).weekday() + 1)
    
    for y, row in enumerate(pixel_values):
        for x, value in enumerate(row):
            if value == 1:
                commit_date = start_date + timedelta(weeks=x, days=y)
                commit_date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')
                subprocess.run(['git', 'commit', '--allow-empty', '-m', 'Commit for pixel art', '--date', commit_date_str])

def add_single_commit(message, commit_date):
    commit_date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')
    subprocess.run(['git', 'commit', '--allow-empty', '-m', message, '--date', commit_date_str])

pixel_values = read_csv('pixel_values.csv')
selected_year = 2022
#create_commits(pixel_values, selected_year)

test_commit_message = "Test commit"
test_commit_date = datetime(2022, 1, 1, 12, 0, 0)
#add_single_commit(test_commit_message, test_commit_date)


def get_commit_hash_before_message(message):
    try:
        log_output = subprocess.check_output(['git', 'log', '--grep', message, '--pretty=format:%H']).decode('utf-8')
        commit_hashes = log_output.split('\n')
        if commit_hashes and commit_hashes[0]:
            first_commit_with_message = commit_hashes[-1]
            parent_commit = subprocess.check_output(['git', 'rev-parse', first_commit_with_message + '^']).decode('utf-8').strip()
            return parent_commit
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    return None

def reset_to_commit(commit_hash):
    try:
        subprocess.run(['git', 'reset', '--hard', commit_hash], check=True)
        print(f"Successfully reset to commit: {commit_hash}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during reset: {e}")

message_to_search = "Commit for pixel art"
commit_hash_before_message = get_commit_hash_before_message(message_to_search)

if commit_hash_before_message:
    reset_to_commit(commit_hash_before_message)
else:
    print(f"No commits found with message: {message_to_search}")
