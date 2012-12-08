"""\
Usage:
  dot.py [options] [<path>] [<address>]
  dot.py -h | --help
  dot.py --version

Where:
  <path> is the file to serve
  <address> is what to listen on, of the form <host>[:<port>], or just <port>
"""

import sys
from docopt import docopt
from path_and_address import resolve, split_address


def main(args=None):
    """The entry point of the application."""
    if args is None:
        args = sys.argv[1:]

    # Parse command-line
    args = docopt(__doc__, argv=args)

    # Parse arguments
    path, address = resolve(args['<path>'], args['<address>'])
    host, port = split_address(address)

    if path is None:
        path = '.'
    if host is None:
        host = 'localhost'
    if port is None:
        port = 5000

    # Run server
    print ' * Serving %s on http://%s:%s/' % (path, host, port)


if __name__ == '__main__':
    main()
