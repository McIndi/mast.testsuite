import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mast.testsuite",
    version = "2.2.0",
    author = "Clifford Bressette",
    author_email = "cliffordbressette@mcindi.com",
    description = ("Test suite for MAST for IBM DataPower"),
    license = "GPLv3",
    keywords = "unit test integration regression suite",
    url = "http://github.com/mcindi/mast.testsuite",
    install_requires=["mock"],
    namespace_packages=["mast"],
    packages=['mast',
              'mast.testsuite',
              'mast.testsuite.unit',
              'mast.testsuite.integration',
              'mast.testsuite.regression'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPLv3",
    ],
)
