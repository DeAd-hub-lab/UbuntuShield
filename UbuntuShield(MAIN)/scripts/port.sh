#!/bin/bash

list_open_ports() {
    netstat -tuln | grep 'LISTEN'
}


main() {
    OPEN_PORTS=$(list_open_ports)
    if [ -z "$OPEN_PORTS" ]; then
        zenity --info --text="No open ports found. Exiting."
        exit 0
    fi

       PORTS_TEXT=$(echo "$OPEN_PORTS" | awk '{print "FALSE", $4}')

      PORTS_TO_CLOSE=$(zenity --list --checklist --title="Select Ports to Close" --text="Select ports to close:" --column="Select" --column="Port" --separator=" " $PORTS_TEXT)

    if [ -z "$PORTS_TO_CLOSE" ]; then
        zenity --info --text="No ports selected to close. Exiting."
        exit 0
    fi

    close_ports "$PORTS_TO_CLOSE"
}

close_ports() {
    PORTS=$1
    for PORT in $PORTS; do
        PORT_NUMBER=$(echo "$PORT" | awk '{print $2}')
        sudo iptables -A INPUT -p tcp --dport "$PORT_NUMBER" -j DROP
        echo "Port $PORT_NUMBER blocked successfully."
    done
}

main
