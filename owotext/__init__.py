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
__license__ = 'ISC'
__copyright__ = 'Copyright 2020 DerpyChap'
__version__ = '1.0.2'

from collections import namedtuple
from .owo import OwO

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(
major=1, minor=0, micro=1, releaselevel='final', serial=0)
