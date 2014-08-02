"""\
Path-and-Address
----------------

Functions for command-line server tools used by humans.

:copyright: (c) 2012 by Joe Esposito.
:license: MIT, see LICENSE for more details.
"""

__version__ = '1.0.0'


from .parsing import resolve, split_address
from .validation import valid_address, valid_hostname, valid_port
