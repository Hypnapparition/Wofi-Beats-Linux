#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 03 12:19:18 PM 2025

@author: Hypnapparition

Created based on Rofi-Beats-Linux by pfitzn (https://github.com/pfitzn/Rofi-Beats-Linux).
"""

# Import modules. There are all built-in in Python3
import subprocess as s
from pathlib import Path
import sys
import json

# Define path to the stations.json file and lib-install.py script
script_dir = Path(__file__).parent.resolve()
stations_file = script_dir / 'config' / 'stations.json'
lib_install_script = script_dir / 'lib-install.py'

s.run(['pkill', '-f', 'radio-mpv'])

# Check if the stations.json file exists
if not stations_file.exists():
    print("Stations file not found. Running lib-install.py to install dependencies...")
    
    # Check if lib-install.py exists before running it
    if not lib_install_script.exists():
        print("lib-install.py not found. Exiting.")
        sys.exit(1)
    
    # Run the lib-install.py script
    s.run(["python3", str(lib_install_script)])
    
    # After running lib-install.py, check again if the stations file exists
    if not stations_file.exists():
        print("The stations file is still missing. Exiting.")
        sys.exit(1)

# Get stations from json file
with open(stations_file) as f:
    radios = json.load(f)
    print(radios)

# Get launcher from file
with open(script_dir / 'config' / 'launcher_config.txt', 'r') as f:
    launcher = f.read().strip()

# Declare where the output of the player will be written, and its name. 
# By default it will be stored in the script's directory. 
# This output is only relevant if it is captured by other programs. 

output_file_dir = script_dir
output_file_name = 'wofi-beats_out.txt'

# Dinamically add a numerical prefix to the radio stations based on the order
# they appear in the `stations.json`. This is done to respect Carbon-Bl4ck's
# original format, and to allow users to edit the radio dictionary without
# needing to maintain the numbers in the station names.

choices = []
index = 0
for i in radios:
    index = index+1
    choices.append(f"{str(index)}. {i}")

# Compile list to be passed to Wofi

choicelist = "\n".join(choices)

# Pass list to Wofi and capture user input

if launcher == 'wofi':
    p1 = s.Popen(["echo", choicelist], stdout=s.PIPE)
    p2 = s.Popen(["wofi", "-dmenu", "-i"], stdin=p1.stdout, stdout=s.PIPE)
elif launcher == 'rofi':
    p1 = s.Popen(["echo", choicelist], stdout=s.PIPE)
    p2 = s.Popen(["rofi", "-dmenu", "-i"], stdin=p1.stdout, stdout=s.PIPE)

p1.stdout.close()

output = p2.communicate()[0].decode()[:-1]

# Remove the number we just added

cleanoutput = " ".join(output.split()[1:])

# If there is an error, notify user and stop execution

if cleanoutput in radios:
    url = radios[cleanoutput]['URL']
else:
    s.run(["notify-send", "Station not found"])
    sys.exit()

# Try to close any current instance of mpv

try:
    s.run(['pkill', '-f', 'radio-mpv'])
except:
    pass

# Clear existing output file if found. This is done so that the file does not
# get huge after many executions
print('1')
s.run(['rm', f"{output_file_dir}/{output_file_name}"])
print('2')
# Open player with URL of selected station, send notification, write output to
# file

with open(f"{output_file_dir}/{output_file_name}", 'w') as f:
    print('3')
    s.run(["notify-send", f"Playing now: \"{radios[cleanoutput]['notification']}\"", "--icon=media-tape"])
    print('4')
    s.run(["mpv", f"{url}", "--idle=yes", "--volume=60", "--title=\"radio-mpv\"", "--input-ipc-server=/tmp/mpvsocket"], stdout=f)
