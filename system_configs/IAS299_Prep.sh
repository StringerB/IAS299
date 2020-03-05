#!/bin/bash -e

echo 'Making scripts folder and sub directories...'
if [ -d /opt/scripts ]
then
	echo 'Scripts exists'
else
	mkdir /opt/scripts
fi

if [ -d /opt/scripts/system_configs ]
then
	echo 'Sys configs exists'
else
	mkdir /opt/scripts/system_configs
fi

if [ -d /opt/scripts/python ]
then
	echo 'Python scripts folder exists'
else
	mkdir /opt/scripts/python
fi

