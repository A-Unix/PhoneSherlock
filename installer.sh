#!/bin/bash

echo -e "\nChecking if Pip3 is already installed\n"

# Check if python3-pip is already installed
if python3 -c "import pkg_resources; pkg_resources.get_distribution('pip')" >/dev/null 2>&1; then
    echo -e "\nPip3 is already installed.\n"
else
    echo -e "\nOops! Pip3 not found on your system, don't worry, I'm installing it for you :)\n"
    sleep 1
    echo -e "\nInstalling Pip3 now!\n"
    sleep 1

    # Install python3-pip using apt
    apt install python3-pip -y
    sleep 1

    echo -e "Done!\n"
fi

# Check if colorama is already installed
if python3 -c "import pkg_resources; pkg_resources.get_distribution('colorama')" >/dev/null 2>&1; then
    echo "Colorama is already installed."
else
    echo -e "Oops! Colorama not found on your system, don't worry, I'm installing it for you :)\n"
    sleep 2

    # Install colorama using pip
    pip install colorama

    echo -e "\nDone! Colorama has been installed successfully.\n"
fi

# Clear the screen
clear
sleep 1

# Check if git is already installed
if ! command -v git &>/dev/null; then
    echo "Git is not installed. Installing it now, please wait."
else
    # Install git using apt
    apt install git -y

    echo -e "\nDone! git has been installed successfully.\n"
fi

repository_url='https://github.com/Atuls-git/kali-anonsurf.git'
script_folder='kali-anonsurf'

# Check if kali-anonsurf is already installed
if ! dpkg -s kali-anonsurf &>/dev/null; then
    echo "Installing kali-anonsurf..."
    sudo apt-get update
else

    # Clone the repository
    echo "Cloning into the repository!"
    git clone "$repository_url"
    echo -e "\e[32mDone!\n\e[0m"

    # Move to the cloned folder
    cd "$script_folder" || exit 1

    # Set necessary permissions
    chmod +x installer.sh

    # Install the script
    ./installer.sh

    echo -e "\e[36mRunning the program now, please wait!\n\e[0m"

    # Start the script
    anonsurf start

    # Give a success message to the user
    echo -e "\e[32mDone! You're undercover now ;)\n\e[0m"

    cd ..
fi

# Get executive permissions for the main script
chmod +x phonesherlock.py

# Run the main script
python3 phonesherlock.py
