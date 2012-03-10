#!/usr/bin/python

"""
Main script for testing pyRCD package

No arguments at this time.
"""

#hack for emacs/ipython during dev
import os
import sys

if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd())
#end hack


from pyRCD.conf    import settings
from pyRCD.utils   import logger

@logger.log_and_call('entering main.py:main()')
def main():
    pass

if __name__ == '__main__':
    main()
