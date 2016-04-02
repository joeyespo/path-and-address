from setuptools import setup, find_packages


setup(
    name='path-and-address',
    version='1.0.0',
    description='Functions for server command-line arguments used by humans.',
    long_description=__doc__,
    author='Joe Esposito',
    author_email='joe@joeyespo.com',
    url='http://github.com/joeyespo/path-and-address',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    install_requires=[],
)
