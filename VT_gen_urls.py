__author__ = 'sparklingSky'

import ipcalc

f = open('VT_links.txt', 'w')
subnet = raw_input('Enter subnet with prefix in format 1.2.3.0/24: ')

for x in ipcalc.Network(subnet):
    f.write('https://www.virustotal.com/en/ip-address/' + str(x) + '/information/' + '\n')
f.close()

print 'Completed. See the result in file VT_links.txt'
