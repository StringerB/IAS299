#!/bin/bash -e

echo 'Installing utilities...'
apt-get install -y vim tmux python3-pip

pip3 install github3.py
pip3 install python3-nmap scapy-python3 scrapy pygeoip mechanize beautifulsoup4


echo 'Getting configs...'
if [ -d /tmp/confs ]
then
	echo '[*] The /tmp/config dir exists.'
else
	mkdir /tmp/confs
	cd /tmp/confs
	git clone https://github.com/jwrenx/Linux_configs.git
	cd /tmp/confs/Linux_Configs
	mv .vimrc ~
	cd ~
fi

#rm -rf /tmp/confs
