# cls = lambda: print("\033[2J\033[;H", end='')
# cls()
import os
import pyfiglet
import colorama
from colorama import Fore
# title
title = pyfiglet.figlet_format("PYTHON-POWER ")
print(Fore.LIGHTRED_EX + title)
print(Fore.RESET)
print('All Devices Ip Scanner: ')
print('----------------------- ')
print()

# Open the ip_list.txt file containing the list of ip addresses
with open('C:/Users/ytzhak/Documents/Python Scripts/ip_list.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
#print(dump)

# Ping each ip address in the list and write the result to output.txt file
for i in dump:
    ip = i.split()[1]
    host = i.split()[0]
    print(Fore.LIGHTCYAN_EX +host)
    print(Fore.RESET + ip)
    res = os.popen(f'ping {ip} -n 2').read()
    #print(res)
    if ("Request timed out" in res) or ("Destination host unreachable" in res):
        print(res)
        f = open('C:/Users/ytzhak/Documents/Python Scripts/output.txt', 'a')
        f.write(str(host) + '\t' + str(ip) + '\tMachine is down' + '\n')
        f.close()
    else:
        print(res)
        f = open('C:/Users/ytzhak/Documents/Python Scripts/output.txt', 'a')
        f.write(str(host) + '\t' + str(ip) + '\tMachine is up' + '\n')
        f.close()

# Open output.txt file
with open('C:/Users/ytzhak/Documents/Python Scripts/output.txt') as file:
    output = file.read()
print(output)

Delete content of output.txt file
with open('C:/Users/ytzhak/Documents/Python Scripts/output.txt', 'w'):
    pass

input("Press any key to quit")

'

