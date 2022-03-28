#!/bin/bash
echo "Please enter name for raspberry pi"
read pi_name
echo "Is this an entry or exit sensor?"
read pi_usage
lxterminal -e sudo python3 QRreader.py $pi_name $pi_usage $1
lxterminal -e sudo python3 RFIDreader.py $pi_name $pi_usage $1
sudo python3 exitButton.py $pi_name $pi_usage $1
