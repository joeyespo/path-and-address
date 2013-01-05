from itertools import product
from ..validation import valid_address, valid_hostname, valid_port


def _join(host_and_port):
    return '%s:%s' % host_and_port


def _join_all(hostnames, ports):
    return map(_join, product(hostnames, ports))


hostnames = [
    '0.0.0.0',
    '127.0.0.1',
    'localhost',
    'example.com',
    'example.org',
]
invalid_hostnames = [
    'http://example.com',
    'http://example.com:8080',
    'example.com/',
    'example.com:8080/',
    'example.com:0',
    '0.0.0.0:0',
]


ports = [1, 80, 5000, 8080, 65535]
invalid_ports = [None, -80, -1, 0, 65536, 75000,
    float('nan'), '', 'nan', 'hello', 'a string']


addresses = hostnames + ports + _join_all(hostnames, ports)
invalid_addresses = invalid_hostnames \
    + _join_all(hostnames, invalid_ports) \
    + _join_all(invalid_hostnames, ports) \
    + _join_all(invalid_hostnames, invalid_ports)


def test_valid_address():
    for address in addresses:
        assert valid_address(address), 'Invalid address, expected to be valid: ' + repr(address)

    for address in invalid_addresses:
        assert not valid_address(address), 'Valid address, expected to be invalid: ' + repr(address)


def test_valid_hostname():
    for hostname in hostnames:
        assert valid_hostname(hostname), 'Invalid hostname, expected to be valid: ' + repr(hostname)

    for hostname in invalid_hostnames:
        assert not valid_hostname(hostname), 'Valid hostname, expected to be invalid: ' + repr(hostname)


def test_valid_port():
    for port in ports:
        assert valid_port(port), 'Invalid port, expected to be valid: ' + repr(port)

    for port in invalid_ports:
        assert not valid_port(port), 'Valid port, expected to be invalid: ' + repr(port)
