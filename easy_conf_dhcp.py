import os




restart = "CACA"

while restart != "Y":
        internal_ip = input("Whitch IP do you want?[x.x.x.x]: ")
        set_ip_conf = ("sed -i 's/10.0.0.1/{}/g' '/etc/netplan/static.yaml'".format(internal_ip))
        
        os.system(set_ip_conf)
        print("[+] Set IP = {}".format(internal_ip))
        
        os.system("netplan apply")
        print("ip changed")
        
        os.system("ping -c 2 8.8.8.8")
        restart = input("¿ping google?[Y/N] ")
        
        if restart == "Y":
            print("[+] configuring DHCP ...")
            
            #Change str to list.

            def split_str(a, c):
                list(a)
                ip_list = a.split('.')
                ip_list.pop(3)
                ip_list.append(c)
                b = ip_list
                return b

            ip_split = split_str(internal_ip, "0")
            
            #Change list to IP.
            
            def list_to_str(a):  
                fina = ""  
                for x in a:
                    fina += x 
                    fina += "."
                b = fina[:-1]
                return b
            
            #DHCP configuration
                        
            getaway = ("sed -i 's/10.10.0.1/{}/g' '/etc/dhcp/dhcpd.conf'".format(internal_ip))
            print("[+] Setted IP GETAWAY: {} ".format(internal_ip))
            
            os.system(getaway)
            
            internal_ip = list_to_str(ip_split)
            
            #Net IP for DHCP

            net_ip = ("sed -i 's/10.10.0.0/{}/g' '/etc/dhcp/dhcpd.conf'".format(internal_ip))
            print("[+] Setted NET IP: {} ".format(internal_ip))
            os.system(net_ip)
            
            #Minnor number of the net.

            minnor = input("Set de minnor IP of the subnet?: ")
            
            
            ip_minnor_split = split_str(internal_ip, minnor)
            minnor_ip = list_to_str(ip_minnor_split)
                      
            less_ip = ("sed -i 's/10.10.0.20/{}/g' '/etc/dhcp/dhcpd.conf'".format(minnor_ip))
            os.system(less_ip)
            print("[+] Setted minnor IP : {}".format(minnor_ip))
            
           #Biggest ip.

            max = input("Set de biggest IP of the subnet?: ")

            ip_biggest_split = split_str(internal_ip, max)
            biggest_ip = list_to_str(ip_biggest_split)


            print("[+] Setted biggest IP : {}".format(biggest_ip))

            ip_max = ("sed -i 's/10.10.0.40/{}/g' '/etc/dhcp/dhcpd.conf'".format(biggest_ip))    
            os.system(ip_max)

            #Restarting of the server
            
            print("[+] Restarting server DHCP")
            os.system("service isc-dhcp-server restart")
            os.system("service isc-dhcp-server status")

            #Routing.

            print("[+] Making route ...")
            os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
            os.system("iptables -A FORWARD -j ACCEPT")
            enrutamineto_final = ("iptables -t nat -A POSTROUTING -s {}/24 -o enp0s3 -j MASQUERADE".format(internal_ip))
            os.system(enrutamineto_final)
            print("[+] Ruted ;D")

            print("All pakages're redirected for the IP: {} ".format(internal_ip))

print("All It's Okey running. Have a fun ;D")
