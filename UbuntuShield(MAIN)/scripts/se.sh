#!/bin/bash

is_selinux_enabled() {
    if [ -f /etc/selinux/config ]; then
        selinux_status=$(grep '^SELINUX=' /etc/selinux/config | awk -F= '{print $2}')
        if [ "$selinux_status" = "disabled" ]; then
            zenity --info --title="SELinux Status" --text="SELinux is currently disabled."
            return 1
        else
            zenity --info --title="SELinux Status" --text="SELinux is currently enabled."
            return 0
        fi
    else
        zenity --error --title="Error" --text="SELinux configuration file not found."
        return 2
    fi
}

enable_selinux() {
    sudo sed -i 's/^SELINUX=disabled/SELINUX=enforcing/' /etc/selinux/config
    zenity --info --title="SELinux Enabled" --text="SELinux has been enabled. Changes will take effect after reboot."
}

# Function to disable SELinux
disable_selinux() {
    sudo sed -i 's/^SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
    zenity --info --title="SELinux Disabled" --text="SELinux has been disabled. Changes will take effect after reboot."
}

is_selinux_enabled

action=$(zenity --list --title="SELinux" --text="Choose an action:" --radiolist --column="" --column="Action" TRUE "Enable SELinux" FALSE "Disable SELinux")

case $action in
    "Enable SELinux")
        enable_selinux
        ;;
    "Disable SELinux")
        disable_selinux
        ;;
    *)
        zenity --error --title="Error" --text="Invalid choice. Exiting."
        exit 1
        ;;
esac

exit 0
