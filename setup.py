"""\
Path-And-Address
----------------

Functions for server command-line arguments used by humans.


Links
`````

* `Website <http://github.com/joeyespo/path-and-address>`_

"""

__version__ = '0.1'
__description__ = '\n\n'.join(__doc__.split('\n\n')[1:]).split('\n\n\n')[0]


import os
from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='path-and-address',
    version=__version__,
    description=__description__,
    long_description=__doc__,
    author='Joe Esposito',
    author_email='joe@joeyespo.com',
    url='http://github.com/joeyespo/path-and-address',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=read('requirements.txt'),
    zip_safe=False,
    entry_points={},
)
