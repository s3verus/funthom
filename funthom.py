
#funthom
#Created by S3verus
#Date: 10/Dec/2018
#github.com/s3S3verus
#en.severus@gmail.com
#i improve it very soon , please wait...

import os
print("funthom\ncreated by S3verus\n")
print(" 1.change local ip \n 2.change mac address \n 3.local scan \n 4.port scan \n 5.ping ip \n \n 00.install dpndns \n 99.exit \n")
x=input("choose number:\n")
x=int(x)

if x == 1 :
    newip=input("enter new ip: (192.168.1.2)\n")
    newmask=input("new netmask: (255.255.255.0)\n")
    intf=input("enter your interface: (eth0/wlan0)\n")
    os.system("ifconfig eth0 192.168.1.2 netmask 255.255.255.0")
else:
    if x == 2:
        newmac=input("enter new mac address: (00:00:00:00:00:02)\n")
        intf=input("enter your interface: (eth0/wlan0)\n")
        os.system("ifconfig eth0 down")
        os.system("ifconfig eth0 hw ether 00:00:00:00:00:02")
        os.system("ifconfig eth0 up")
    else:
        if x == 3:
            ip=input("enter ip with type: (192.168.1.0/24) \n")
            os.system("nmap -sP 192.168.1.0/24")
        else:
            if x == 4:
                ip=input("enter ip to scan: (192.168.1.1)\n")
                iprng=input("enter range of ports: (for EX: 1-6000)\n")
                os.system("nmap -p 1-6000 192.168.1.1")
            else:
                if x == 5:
                    ip=input("enter ip to ping: (192.168.1.1)\n")
                    os.system("ping 192.168.1.1")
                else:
                    if x == 99:
                        print("tnx for download...")
                        exit()
                    else:
                        if x == 0:
                            print("i will check for nmap...")
                            os.system("apt-get install nmap")
