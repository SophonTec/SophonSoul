"""
------------
SophonSoul
------------

SophonSoul is the soul of AI system.

Usage
-----
::
  >>> 
"""


from setuptools import setup, find_packages
import sys
from sophonsoul import __version__


setup(name='SophonSoul',
      version=__version__,
      author='SophonTec',
      author_email='sophontec@gmail.com',
      description='SophonSoul is the soul of AI system',
      long_description=__doc__,
      # package_dir={'': 'sophonsystem'},
      packages=find_packages(),
      py_modules=['sophonsoul'],
      classifiers=['Development Status :: 2 - PreAlpha',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3.8',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence'
                   ]
      )
