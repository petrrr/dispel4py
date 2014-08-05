import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="dispel4py",
    version="0.0.1",
    author="The University of Edinburgh",
    author_email="a.krause@epcc.ed.ac.uk",
    url="https://github.com/akrause2014/dispel4py",
    license="Apache 2",
    description=(
        "Dispel4py is a Python library used to describe abstract workflows \
        for distributed data-intensive applications."),
    long_description=read('README.md'),
    keywords="dispel4py dispel workflows processing elements",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache 2 License",
    ],
    packages=['dispel4py', 'dispel4py.seismo', 'dispel4py.storm',
              'dispel4py.test', 'dispel4py.test.graph_testing'],
    install_requires=['networkx', 'requests'],
    entry_points={
        'console_scripts': [
            'idispel4py = dispel4py.dispel4py_client:main',
        ]
    },
)
