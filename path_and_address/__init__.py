"""\
Path-and-Address
----------------

Functions for command-line server tools used by humans.

:copyright: (c) 2012 by Joe Esposito.
:license: MIT, see LICENSE for more details.
"""

__version__ = '0.1'


import re


hostname_component_re = re.compile('(?!-)[A-Z\d-]{1,63}(?<!-)$', re.IGNORECASE)


def resolve(path_or_address=None, address=None, *ignored):
    """Returns (path, address) based on consecutive optional arguments, [path] [address]."""
    if path_or_address is None or address is not None:
        return path_or_address, address

    path = None
    if split_address(path_or_address)[1] is not None:
        address = path_or_address
    else:
        path = path_or_address

    return path, address


def split_address(address):
    """Returns (host, port) with an integer port from the specified address string. (None, None) is returned if the address is invalid."""
    invalid = None, None
    if not address:
        return invalid

    components = address.split(':')
    if len(components) > 2 or not valid_hostname(components[0]):
        return invalid

    if len(components) == 2 and not valid_port(components[1]):
        return invalid

    if len(components) == 1:
        components.insert(0 if valid_port(components[0]) else 1, None)

    host, port = components
    port = int(port) if port else None

    return host, port


def valid_address(address):
    """Determines whether the specified address string is valid."""
    if not address:
        return False

    components = address.split(':')
    if len(components) > 2 or not valid_hostname(components[0]):
        return False

    if len(components) == 2 and not valid_port(components[1]):
        return False

    return True


def valid_hostname(host):
    """Returns whether the specified string is a valid hostname."""
    if len(host) > 255:
        return False

    if host[-1:] == '.':
        host = host[:-1]

    return all(hostname_component_re.match(c) for c in host.split('.'))


def valid_port(port):
    """Returns whether the specified string is a valid port."""
    try:
        return 1 <= int(port) <= 65535
    except:
        return False
