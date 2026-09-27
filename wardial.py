'''
Starter functions for the War Dialing lab.
Assignment instructions: https://csci40.rtealwitter.com/topics/09_syntactic_sugar/lab.html
'''

import requests

# Complete each function using its contract and doctests.

def is_server_at_hostname(hostname):
    '''
    A hostname is a generic word for either an IP address or a domain name.
    Your function should return True if `requests.get` is successfully able to connect to the input hostname.

    HINT:
    The input hostname will not contain a scheme,
    and you will have to add it.

    These examples replace the network request with predictable outcomes.
    They work without internet access and restore requests.get after each test.

    >>> from unittest.mock import patch
    >>> with patch('requests.get', return_value=object()):
    ...     is_server_at_hostname('online.test')
    True
    >>> with patch('requests.get', side_effect=requests.ConnectionError):
    ...     is_server_at_hostname('offline.test')
    False
    >>> with patch('requests.get', side_effect=requests.Timeout):
    ...     is_server_at_hostname('slow.test')
    False

    Pass timeout=5 to requests.get. Any HTTP response, including 403 or 404,
    means a server replied. Return False for connection errors and timeouts.
    '''



def increment_ip(ip):
    '''
    Return the "next" IPv4 address.

    >>> increment_ip('1.2.3.4')
    '1.2.3.5'
    >>> increment_ip('1.2.3.255')
    '1.2.4.0'
    >>> increment_ip('0.0.0.0')
    '0.0.0.1'
    >>> increment_ip('0.0.0.255')
    '0.0.1.0'
    >>> increment_ip('0.0.255.255')
    '0.1.0.0'
    >>> increment_ip('0.255.255.255')
    '1.0.0.0'
    >>> increment_ip('0.255.5.255')
    '0.255.6.0'
    >>> increment_ip('255.255.255.255')
    '0.0.0.0'
    '''


def enumerate_ips(start_ip, n):
    '''
    Return a list containing the next `n` IPs beginning with `start_ip`.

    >>> list(enumerate_ips('192.168.1.0', 2))
    ['192.168.1.0', '192.168.1.1']

    >>> list(enumerate_ips('8.8.8.8', 10))
    ['8.8.8.8', '8.8.8.9', '8.8.8.10', '8.8.8.11', '8.8.8.12', '8.8.8.13', '8.8.8.14', '8.8.8.15', '8.8.8.16', '8.8.8.17']

    # This test ensures that you are properly handling "wrap around"
    #
    >>> list(enumerate_ips('192.168.0.255', 2))
    ['192.168.0.255', '192.168.1.0']

    The following tests ensure that the correct number of ips get returned.

    >>> len(list(enumerate_ips('8.8.8.8', 10)))
    10
    >>> len(list(enumerate_ips('8.8.8.8', 1000)))
    1000
    >>> len(list(enumerate_ips('8.8.8.8', 100000)))
    100000
    '''


if __name__ == '__main__':
    # FIXME 1: use enumerate_ips to generate 1024 addresses from 175.45.176.0.
    dprk_ips = []

    # FIXME 2: keep addresses for which is_server_at_hostname returns True.
    # Run this block through `python3 offline_scan.py` while developing.
    dprk_ips_with_servers = []
    print('dprk_ips_with_servers=', dprk_ips_with_servers)
