#i build it very soon , please wait...

print("1.change local ip \n 2.change mac address \n 3.local scan \n 4.port scan \n 5.ping ip \n 99.exit \n")
x=input("enter number")
x=int(x)
if x == 1 :
#    ifconfig eth0 192.168.0.1 netmask 255.255.255.0
else if x == 2:
#    ifconfig eth0 down
#    ifconfig eth0 hw ether 00:00:00:00:00:02
#    ifconfig eth0 up
else if x == 3:
#   nmap -sP 192.168.1.0/24
else if x == 4:
#   nmap -p "*" 192.168.1.10
else if x == 5:
#   ping 192.168.1.1
else if x == 99:
    print("tnx for download...")
    exit()
