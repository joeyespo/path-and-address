from itertools import product
import sys
from ..parsing import resolve, split_address

if sys.version_info[0] >= 3:
    basestring = str

paths = [
    '0.0.0.0',
    './80',
    '.',
    '/file',
    'path/to/file',
    '/path/to/file',
    '\\file',
    'path\\to\\file',
    '\\path\\to\\file',
    'C:\\path\\to\\file',
]
addresses = [
    '80',
    ':80',
    '0.0.0.0:80',
    '127.0.0.1:5000',
    'localhost:8080',
    'example.com:80',
]


hosts = [
    '0.0.0.0',
    '127.0.0.1',
    'localhost',
    'example.com',
    'example.org',
]
ports = [
    80,
    5000,
    8080,
    '80',
    ':80',
]


def test_resolve():
    assert resolve() == (None, None), 'Expected empty result'

    for path in paths:
        p, a = resolve(path)
        assert p == path, 'Expected a path, %s, got %s' % (repr((path, None)), repr((p, a)))

    for host in addresses:
        p, a = resolve(host)
        assert a == host, 'Expected an address, %s, got %s' % (repr((None, host)), repr((p, a)))


def test_split_address():
    for address in hosts:
        host, port = split_address(address)
        assert address == host, 'Expected a host, %s, got %s' % (repr((address, None)), repr((host, port)))

    for address in ports:
        host, port = split_address(address)
        address = str(address).replace(':', '')
        assert address == str(port), 'Expected a port, %s, got %s' % (repr((None, address)), repr((host, port)))

    for h, p in product(hosts, ports):
        if isinstance(p, basestring):
            p = str(p).replace(':', '')
        host, port = split_address('%s:%s' % (h, p))
        assert str(host) == str(h) and str(port) == str(p), 'Expected %s, got %s' % (repr((h, p)), repr((host, port)))
