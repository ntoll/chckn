#!/usr/bin/env python3
from setuptools import setup
from chicken import CHICKEN 


with open("README.md") as f:
    readme = f.read()
with open("CHANGES.md") as f:
    changes = f.read()


setup(
    name="chckn",
    version=CHICKEN,
    description="Chicken chicken chicken chicken 'chicken'. Chicken chicken!",
    long_description=readme + "\n\n" + changes,
    author="Nicholas H.Tollervey",
    author_email="ntoll@ntoll.org",
    url="https://github.com/ntoll/chckn",
    py_modules=["chicken",],
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Topic :: Education",
        "Topic :: Communications",
        "Topic :: Software Development :: Internationalization",
    ],
    entry_points={"console_scripts": ["chicken=chicken:_chicken"],},
)
