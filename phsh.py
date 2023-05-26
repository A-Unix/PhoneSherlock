#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
import os
from os import system as s
import time

print("Please wait!")

# Install colorama using pip
os.system("pip install colorama")
os.system("pip install pyfiglet")

print("Done!")

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
|| This tool was created by Hash30 a.k.a anonymous. ||
|| Please note that i'm not responsible for the misuse of this tool, it has been created for educational purposes only, use it at your own responsibility! ||

'''

print(banner)

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
    exit(0)  # Exit the script
except pkg_resources.DistributionNotFound:
    pass  # Proceed with the installation

print("Oops! Colorama not found on your system, don't worry, I'm installing it for you :)\n")
time.sleep(1)
print("Installing Colorama now!\n")
time.sleep(1)

# Install colorama using pip
subprocess.check_call(["pip", "install", "colorama"])

from colorama import init, Fore
# Initialize colorama
init()
print(Fore.GREEN + "Done! Now you can see the result of installing Colorama in this line :)")

time.sleep(1)

print(Fore.BROWN + "Checking if Pip3 is already installed")

# Check if python3-pip is already installed
try:
    dist = pkg_resources.get_distribution('pip')
    print(Fore.GREEN + "Pip3 is already installed.")
    exit(0)  # Exit the script
except pkg_resources.DistributionNotFound:
    pass  # Proceed with the installation

print(Fore.RED + "Oops! Pip3 not found on your system, don't worry, I'm installing it for you :)\n")
time.sleep(1)
print(Fore.GREEN + "Installing Pip3 now!\n")
time.sleep(1)

# Install python3-pip using apt
subprocess.check_call(["apt", "install", "python3-pip", "-y"])

print("Done!")
input(Fore.CYAN + "Press Enter to continue...")

# Specify the website URL
website_url = input(Fore.GREEN + "Please enter webpage url Ex: https://example.com >>> ")

# Send a GET request to the website
response = requests.get(website_url)

# Extract phone numbers using regular expressions
phone_numbers = re.findall(r"\b\d{3}-\d{3}-\d{4}\b", response.text)

# Convert phone numbers to XXXXXXXXXX format
formatted_numbers = [re.sub(r"\D", "", number) for number in phone_numbers]

# Print the converted phone numbers
print(Fore.GREEN + "Indian numbers found:")
for number in formatted_numbers:
    print(Fore.YELLOW + number)

time.sleep(2)

# Print the phone numbers found
print(Fore.GREEN + "Other numbers found:")
for number in phone_numbers:
    print(Fore.BROWN + number)
    
time.sleep(1)
