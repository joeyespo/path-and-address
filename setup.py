"""\
Path-And-Address
----------------

Functions for server command-line arguments used by humans.


Links
`````

* `Website <http://github.com/joeyespo/path-and-address>`_

"""

import os
from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='path-and-address',
    version='0.1',
    description='Functions for server command-line arguments used by humans.',
    long_description=__doc__,
    author='Joe Esposito',
    author_email='joe@joeyespo.com',
    url='http://github.com/joeyespo/path-and-address',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    install_requires=read('requirements.txt'),
    zip_safe=False,
    entry_points={},
)
