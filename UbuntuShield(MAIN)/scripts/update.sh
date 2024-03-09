#!/bin/bash 

zenity --info --text="Updating package lists..." --title="Package Update"
sudo apt update

zenity --info --text="Upgrading packages..." --title="Package Upgrade"
sudo apt upgrade -y

zenity --info --text="Cleaning up..." --title="Package Cleanup"
sudo apt autoremove -y
sudo apt autoclean

zenity --info --text="Update and upgrade complete." --title="Package Update"