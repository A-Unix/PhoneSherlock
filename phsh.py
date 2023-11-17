#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
import os
import time
from colorama import init, Fore

# Initialize colorama
init()

print("Please wait!")

# Install colorama using pip
os.system("pip install colorama")
os.system("pip install pyfiglet")

print("Done!")

os.system("clear")

time.sleep(1)

print("\nWelcome!")

time.sleep(2)

banner = r'''
                                      _ _ _                                        _ _ _                 _ _ _   
                /\       |\      |  /       \   |\      | \       / |\      /|   /       \   |     |   /       \ 
               /  \      | \     | |         |  | \     |  \     /  | \    / |  |         |  |     |  |         |
              /    \     |  \    | |         |  |  \    |   \   /   |  \  /  |  |         |  |     |  |          
             /_ _ _ \    |   \   | |         |  |   \   |    \ /    |   \/   |  |         |  |     |   \_  _ _   
            /        \   |    \  | |         |  |    \  |     |     |        |  |         |  |     |           \ 
           /          \  |     \ | |         |  |     \ |     |     |        |  |         |  |     |  |         |
          /            \ |      \|  \_ _ _ _/   |      \|     |     |        |   \_ _ _ _/   \_ _ _/  \ _  _  _/ 

|| You may get an error if you do not enter your webpage address correctly. ||
|| This tool was created by Atul a.k.a anonymous. ||
Just so you know, I'm not responsible for the misuse of this tool, it has been created for educational purposes only, and you can use it at your own responsibility! ||
'''

print(banner)

time.sleep(7)

import datetime
now = datetime.datetime.now()
print("Current date and time:")
print(now.strftime("%d-%m-%Y %H:%M:%S"))

time.sleep(2)

import sys
print("Python version:")
print(sys.version)
print("Python version:", sys.version_info)

time.sleep(2)

# Check if the script is running as root
if os.geteuid() != 0:
    print("This script must be run as root")
    exit(1)

print("Checking & Installing required packages\n")

time.sleep(1)

import subprocess
import pkg_resources

# Check if colorama is already installed
try:
    dist = pkg_resources.get_distribution('colorama')
    print('Colorama', dist.version, 'is already installed.')
except pkg_resources.DistributionNotFound:
    print("Oops! Colorama not found on your system, don't worry, I'm installing it for you :)\n")
    time.sleep(2)
    print("Installing Colorama now!\n")
    time.sleep(1)

    # Install colorama using pip
    subprocess.check_call(["pip", "install", "colorama"])

    from colorama import init, Fore
    # Reinitialize colorama after installation
    init()

    print(Fore.MAGENTA + "\nDone! Now you can see the result of installing Colorama in this line :)\n")

os.system("clear")

time.sleep(1)

print(Fore.GREEN + "\nChecking if Pip3 is already installed\n")

# Check if python3-pip is already installed
try:
    dist = pkg_resources.get_distribution('pip3')
    print(Fore.GREEN + "\nPip3 is already installed.\n")
except pkg_resources.DistributionNotFound:
    print(Fore.RED + "\nOops! Pip3 not found on your system, don't worry, I'm installing it for you :)\n")
    time.sleep(1)
    print(Fore.GREEN + "\nInstalling Pip3 now!\n")
    time.sleep(1)

    # Install python3-pip using apt
    subprocess.check_call(["apt", "install", "python3-pip", "-y"])
    time.sleep(1)

    print("Done!\n")

os.system("clear")

# Waiting for user response
input(Fore.GREEN + "Press Enter to continue...")

print(Fore.BLUE + "\n Let's go undercover ;)\n")

repository_url = 'https://github.com/Atuls-git/kali-anonsurf.git'

# Cloning the repo

print("Cloning into the repository!\n")
subprocess.run(['git', 'clone', repository_url])

print("Done!\n")

subprocess.run(['cd kali-anonsurf'])

# Getting necessary permissions
subprocess.run(['chmod +x installer.sh'])

# Installing the script
subprocess.run(['./installer.sh'])

# Start the script
subprocess.run(['anonsurf start'])

# Give a success message to the user
print(Fore.GREEN + "Done! You're undercover now ;)")

# Head back to the main script folder
subprocess.run(['cd ..'])


# Specify the website URL
website_url = input(Fore.BLUE + "Please enter webpage url Ex: https://example.com >>> ")

# Define a function to check the backend process status
def check_website_url_status():
    # Replace this with your actual logic to check the backend process status
    return False

website_url_running = True

while website_url_running:
    print(Fore.BLUE + "[+] Finding Numbers", end="")

    # Blinking effect using a loop
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)  # Delay between each dot

    # Clearing the dots using a backspace character (\b)
    print("\b" * 3, end="", flush=True)
    time.sleep(0.5)  # Delay between removing the dot

    # Check if the backend process has finished
    website_url_running = check_website_url_status()

# Send a GET request to the website
response = requests.get(website_url)

# Extract phone numbers using regular expressions
phone_numbers = re.findall(r"\b\d{3}-\d{3}-\d{4}\b", response.text)

# Convert phone numbers to XXXXXXXXXX format
formatted_numbers = [re.sub(r"\D", "", number) for number in phone_numbers]

# The backend process has finished
print(Fore.CYAN + "[+] Finding Numbers... Done!\n")

time.sleep(1)

# Print the formatted phone numbers
if formatted_numbers:
    print(Fore.GREEN + "\nIndian numbers found:\n")
    for number in formatted_numbers:
        print(Fore.YELLOW + number)
else:
    print(Fore.RED + "\nNo numbers found.\n")

time.sleep(1)

# Print the other numbers
if phone_numbers:
    print(Fore.BLUE + "\nOther numbers found:\n")
    for number in phone_numbers:
        print(Fore.MAGENTA + number)
else:
    print(Fore.RED + "\nNo other numbers found.")

subprocess.run(['anonsurf stop'])
