from distutils.core import setup

from main import (
    __appname__, __version__, __license__, __author__, __url__,
    __email__, __description__
)

setup(
    name=__appname__,
    version=__version__,
    packages=[''],
    url=__url__,
    license=__license__,
    author=__author__,
    author_email=__email__,
    description=__description__,
    options={},
    zipfile=None,
    windows=[{
        "script": "",
        "icon_resources": [],
        "dest_base": ""
    }]
)
