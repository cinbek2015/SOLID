# 01.02.2022

from Ping import IP_scan

name = IP_scan("192.168.0.1", "192.168.0.254")
[print(ip) for ip in name.get_ip()]

def sqard(num: int):
    return(4*num, num*num,  (num*num)*(2*0.5))

print(sqard(12))