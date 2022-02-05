#01.22.2022
"""
Сканирует сегмент сети
"""
from ipaddress import ip_address

class IP_scan:

    def __init__(self, ip_start, ip_finish):
        self._ip_start = ip_address(ip_start)
        self._ip_finish = ip_address(ip_finish)


    def get_ip(self):
        return (self._ip_start, self._ip_finish)
