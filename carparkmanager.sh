#!/bin/bash
lxterminal -e sudo python3 QRreader.py $1
lxterminal -e sudo python3 RFIDreader.py $1
