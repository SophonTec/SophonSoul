"""
------------
SophonSystem
------------

SophonSystem is the computational core of the Sophon-cognitive AI system.
Leveraging modern tensor-based parallel computing power, SophonSystem realizes the
deeplearning and reinforcement learning algorithms with a cognitive core.

Usage
-----
::
  >>> 
"""


from setuptools import setup, find_packages
import sys
from sophonsystem import __version__


setup(name='SophonSystem',
      version=__version__,
      author='SophonTec',
      author_email='sophontec@gmail.com',
      description='SophonSystem is the computational core of the Sophon AI system',
      long_description=__doc__,
      # package_dir={'': 'sophonsystem'},
      packages=find_packages(),
      py_modules=['sophonsystem'],
      classifiers=['Development Status :: 2 - PreAlpha',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3.8',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence'
                   ]
      )
