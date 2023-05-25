#!/bin/bash

# Ensure we are being ran as root
if [ $(id -u) -ne 0 ]; then
	echo "This script must be ran as root"
	exit 1
fi

echo "Checking & installing required packages"

sudo apt update -y && apt install python3-pip -y && pip install pyfiglet

echo "Done!"
read -p "Press Enter to continue..."

# Python banner code
python_banner=$(python - <<END
import pyfiglet

banner_text = "banner"

banner_text = " 

                                      _ _ _                                        _ _ _                 _ _ _   
                /\       |\      |  /       \   |\      | \       / |\      /|   /       \   |     |   /       \ 
               /  \      | \     | |         |  | \     |  \     /  | \    / |  |         |  |     |  |         |
              /    \     |  \    | |         |  |  \    |   \   /   |  \  /  |  |         |  |     |  |          
             /_ _ _ \    |   \   | |         |  |   \   |    \ /    |   \/   |  |         |  |     |   \_  _ _   
            /        \   |    \  | |         |  |    \  |     |     |        |  |         |  |     |           \ 
           /          \  |     \ | |         |  |     \ |     |     |        |  |         |  |     |  |         |
          /            \ |      \|  \_ _ _ _/   |      \|     |     |        |   \_ _ _ _/   \_ _ _/  \ _  _  _/ 

| You may get an error if you do not enter your webpage address correctly.
| This tool was created by Hash30 a.k.a anonymous.
| Please note that i'm not responsible for the misuse of this tool, it has been created only for educational purposes, use it at your own responsibility!
"

banner = pyfiglet.Figlet().renderText(banner_text)
print(banner)
END
)

# Display the Python banner
echo "$python_banner"
read -p "Press Enter to continue..."

# Update/Upgrade system
echo "Please wait while we update and fix your system to ensure that script works seemlessly... Hold your horses :)"
sudo apt update && apt dist-upgrade -y && apt --fix-broken install -y && apt autoremove -y

echo "Update done! Thanks for your patience"
read -p "Press Enter to continue..."

echo "Now, let's make you ANONYMOUS to ensure that you do not get caught ;)"
read -p "Press Enter to continue..."

echo "Goin undercover!"
read -p "Press Enter to continue..."

echo "Importing required package"
git clone https://github.com/Anonymous-Hash30/anonymous.script.git
echo "Import done!"

echo "Entering into script folder"
cd anonymous.script
echo "Entered!"

echo "Getting required permissions"
chmod +x installer.sh
echo "Done!"

echo "Running the script now, please keep patience!"
./installer.sh
echo "Thanks for your paitence, you are ANONYMOUS now :)"

cd ..

echo "Let's gets started now ;)"



# Specify the website URL
website_url="https://example.com"

# Fetch the website content using curl
website_content=$(curl -s "$website_url")

# Use grep with a regular expression to find phone numbers
phone_numbers=$(echo "$website_content" | grep -Eo '[0-9]{3}-[0-9]{3}-[0-9]{4}')

# Count the number of phone numbers found
count=$(echo "$phone_numbers" | wc -l)

# Display the phone numbers and count
echo "Phone Numbers found on $website_url:"
echo "$phone_numbers"
echo "Total Count: $count"
