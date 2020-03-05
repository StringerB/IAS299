#!/bin/bash -e

echo 'Updating...'
apt-get update 

echo 'Upgrading...'
apt-get upgrade -y && apt-get dist-upgrade -y

echo 'Removing legacy...'
apt-get auto-remove -y

