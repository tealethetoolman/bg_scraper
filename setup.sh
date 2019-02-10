#!/usr/bin/env bash
sudo apt update
sudo apt-get install -y python3 python3-pip
sudo pip3 install --upgrade pip
for DEP in $(cat requirements.txt); do
sudo pip3 install $DEP
done
