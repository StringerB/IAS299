#!/usr/bin/python3

#Imports
import urllib3
import threading
import os
from bs4 import BeautifulSoup

#Variables
threads = 1
target = 'http://testphp.vulnweb.com/'
wordlist = '/usr/share/amass/wordlists/all.txt'
header={}
header['User-Agent'] = 'Googlebot'
raw_words = []
resume = None

os.chdir('/home/jeremy/Downloads/dirbuster_results/')

#Set the pool manager
req = urllib3.PoolManager()

def build_wordlist():
    #read in the wordlist
    with open(wordlist, 'r') as wl:
        raw_words = wl.readlines()
    found_resume = False
    words = []
    for word in raw_words:
        word = word.rstrip()
        if resume is not None:
            if found_resume:
                words.append(word)
            else:
                if word == resume:
                    found_resume = True
                    print('Resuming wordlist from {}'.format(resume))
        else:
            words.append(word)
    print('[*] Wordlist complete...')
    return words


def dir_bruter(wordl, extensions=None):
    while len(wordl) != 0:
        for word in wordl:
            attempt = word
            attempt_list = []
            #check for file extensions
            #if not, we assume its a dir
            if '.' not in attempt:
                attempt_list.append('/{}/'.format(word))
            else:
                attempt_list.append('/{}'.format(word))      
            #allow extensions
            if extensions:
                for extension in extensions:
                    attempt_list.append('{}{}'.format(attempt,extension))
            #iterate over list
            for brute in attempt_list:
                try:
                    url = '{}{}'.format(target,attempt)
                    result = req.request('GET', url, headers=header)
                    soup = BeautifulSoup(result.data, 'html.parser')

                    if '404 Not Found' in soup.find('title'):
                        continue
                    else:
                        #print('[*] Bruteforcing: {}\n'.format(url))
                        #with open('{}'.format(attempt), 'w+') as f:
                        #    f.write(soup)
                        print(soup)

                except urllib3.exceptions.ResponseError as e:
                    if hasattr(e, 'code'):
                        print('[!!!] {} => {}'.format(e, url))
                    else:
                        print('[!!!!] Oh no...')
                    pass

word_queue = build_wordlist()
extensions = ['.php','.bak','.orig','.inc']

for i in range(threads):
    t = threading.Thread(target=dir_bruter, args=(word_queue,extensions,))
    t.start()


#EOF