#!/bin/bash

# Get files from Google Drive
# Source: https://stackoverflow.com/a/50573452/2382312
# Usage: download_gdrive FILE_ID DESTINATION_PATH

# $1 = file ID
# $2 = file name

URL="https://drive.google.com/uc?export=download&id=$1"

wget --load-cookies /tmp/cookies.txt "https://drive.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate $URL -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$1" -O $2 && rm -rf /tmp/cookies.txt


