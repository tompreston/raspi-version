from __future__ import with_statement

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import raspi_version


raspi_version_classifiers = [
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]


with open("README.md", "r") as fp:
    raspi_version_long_description = fp.read()


setup(
    name="raspi_version",
    version=raspi_version.__version__,
    author="Thomas Preston",
    author_email="thomasmarkpreston+raspiversion@gmail.com",
    url="https://github.com/tompreston/raspi-version",
    py_modules=["raspi_version"],
    description="Python 2 and 3 compatibility utilities",
    long_description=raspi_version_long_description,
    license="MIT",
    classifiers=raspi_version_classifiers
)
