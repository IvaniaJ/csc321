import netifaces
def get_interfaces():
    """Return a list of all the interfaces on this host

    Args: None

    Returns: (list) List of interfaces for this host
    """
    return netifaces.interfaces()
print(get_interfaces())

def get_mac(interface: str):
    """For the given interface string, return the MAC address as a
    string

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (str) MAC address
    """
    addrs = netifaces.ifaddresses(interface)
    return addrs[netifaces.AF_LINK][0]['addr']
print(get_mac('{9E827DC7-575D-4BA5-81B7-F69AFD6E85DF}'))

def get_ips(interface: str):
    """For the given interface string, return a dictionary with
    the IPv4 and IPv6 address objects for that interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Address('192.168.65.48'),
       'v6': ipaddress.IPv6Address('fe80::14e1:8686:e720:57a')}
    """
    try:
        addrs = netifaces.ifaddresses(interface)
        return addrs[netifaces.AF_INET][0]['addr']
    except KeyError:
        return addrs[netifaces.AF_INET6][0]['addr']
print(get_ips('{9E827DC7-575D-4BA5-81B7-F69AFD6E85DF}'))

def get_netmask(interface: str):
    """For the given interface string, return a dictionary with the
    IPv4 and IPv6 netmask objects (as IPv4/v6Address objects) for that
    interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Address('255.255.255.0'),
       'v6': ipaddress.IPv6Address('ffff:ffff:ffff:ffff::')}
    """
    try:
        addrs = netifaces.ifaddresses(interface)
        return addrs[netifaces.AF_INET][0]['netmask']
    except KeyError:
        return addrs[netifaces.AF_INET6][0]['netmask']
print(get_netmask('{9E827DC7-575D-4BA5-81B7-F69AFD6E85DF}'))

def get_network(interface: str):
    """For the given interface string, return a dictionary with
    the IPv4 and IPv6 network objects for that interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Network('192.168.65.0/24'),
       'v6': ipaddress.IPv6Network('fe80::/64')}
    """
    try:
        addrs = netifaces.ifaddresses(interface)
        return addrs[netifaces.AF_INET]
    except KeyError:
        return addrs[netifaces.AF_INET6]
print(get_network('{9E827DC7-575D-4BA5-81B7-F69AFD6E85DF}'))
