# This simple script copies the code.py file from this repo to the root of
# the E drive.  It makes it possible to have the Python code inside of GitHub
# but easily deploy the actual program to the Circuit Express.

import os

# Define the source and destination paths
# source_path is wherever this file is located along with the nearby code.py file
source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'code.py')
# destination_path is static and needs updating if Circuit_Express doesn't mount as e drive
destination_path = 'e:\\code.py'

# Use the os module to execute a shell command that copies the file
os.system(f'copy {source_path} {destination_path}')