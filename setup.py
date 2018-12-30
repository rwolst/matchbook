
from setuptools import setup, find_packages
from matchbook import __version__

setup(
    name="matchbook",
    version=__version__,
    author="Rory Cole",
    author_email="rory.cole1990@gmail.com",
    description="Matchbook API Python wrapper",
    url="https://github.com/rozzac90/matchbook",
    packages=find_packages(),
    install_requires=['requests==2.13.0',
                      'python-dateutil==2.6.0',
                      'pytz==2017.2'],
    long_description=open('README.md').read(),
    tests_require=['pytest'],
)
