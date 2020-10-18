#!/bin/sh
# Install required packages
pip3 install -r requirements.txt --user

# Install ffmpeg and imagemagick
sudo apt-get install ffmpeg imagemagick 