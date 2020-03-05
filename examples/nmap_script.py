#!/usr/bin/python3
import nmap3

scanner = nmap3.NmapScanTechniques()
#results = scanner.nmap_ping_scan('8.8.8.8')


host = '192.168.1.'

for item in range(1, 255):
    results = scanner.nmap_ping_scan(host+str(item))
    print(results)
    print('')
