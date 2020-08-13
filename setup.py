import setuptools

from main import (
    __appname__, __version__, __license__, __author__, __url__,
    __email__, __description__
)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=__appname__,
    version=__version__,
    packages=setuptools.find_packages(),
    url=__url__,
    license=__license__,
    author=__author__,
    author_email=__email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
    ],
    python_requires='>=3.7',
)
