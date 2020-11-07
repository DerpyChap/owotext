# -*- coding: utf-8 -*-
"""
owotext
~~~~~~~~~~~~~~~~~~~
A Python library for converting text strings into OwO
:copyright: (c) 2020 DerpyChap
:license: MIT, see LICENSE for more details.
"""

__title__ = 'owotext'
__author__ = 'DerpyChap'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 DerpyChap'
__version__ = '1.1.1'

from collections import namedtuple
from .owo import OwO

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=1, minor=1, micro=1, releaselevel='final', serial=0)
