#!/usr/bin/env bash

# install apt-packages
sudo apt install python3-pip
sudo apt install python3-gpiozero
sudo apt install pipenv
sudo apt install git


# install 1password commandline tool (https://support.1password.com/command-line-getting-started/)
wget https://cache.agilebits.com/dist/1P/op/pkg/v1.10.0/op_linux_arm_v1.10.0.zip
unzip op_linux_arm_v1.10.0.zip
mv op ~/.local/bin
rm op*

# execte .profile to ensure that PATH is set correctly
source ~/.profile


