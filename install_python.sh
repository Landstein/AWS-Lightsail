#!/bin/bash
echo "Installing Python3.7" 
sudo apt update
sudo apt install software-properities-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.7
python3.7 --version 
echo "python3.7 is installed"
echo "---------------------"
echo "---------------------"
echo "---------------------"
echo "---------------------"
echo "Installing pip3"
sudo apt update
sudo apt install python3-pip
pip3 --version 
echo "pip3 installed"