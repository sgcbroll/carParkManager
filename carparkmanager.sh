#!/bin/bash
echo "Please enter name for raspberry pi"
read piname
echo "Is this an entry or exit sensor?"
lxterminal -e sudo python3 QRreader.py $1
lxterminal -e sudo python3 RFIDreader.py $1
