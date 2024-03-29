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
    apt update
    apt install python3-pip -y
    sleep 1

    echo -e "Done!\n"
fi

apt update
apt dist-upgrade -y
apt --fix-broken install -y
apt --fix-missing install -y
apt autoremove -y

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

# Check if git is already installed
if ! command -v git &>/dev/null; then
    echo "Git is not installed. Installing it now, please wait."
    apt install git -y
    echo -e "\nDone! git has been installed successfully.\n"
fi

apt-get install dos2unix -y
pip install requests

dos2unix installer.sh

apt install python2 -y
