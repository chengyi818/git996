#!/usr/bin/env python3
# Author: ChengYi
# Mail: chengyi818@foxmail.cn
# created time: Fri 19 Apr 2019 09:40:27 AM CST

"""
Setup
"""

from setuptools import setup, find_packages


def find_version(file_name):
    with open(file_name) as file_handle:
        lines = file_handle.readlines()
        latest_version = lines[0].strip("\n").rstrip(']').lstrip('[')
        print("git996:", latest_version)
        return latest_version


setup(
    name="git996",
    version=find_version("./ChangeLog"),
    description="One command to sync multiple git repositories",
    author="chengyi",
    author_email="chengyi818@foxmail.com",
    url="https://github.com/chengyi818/git996",
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['toml',
                      'arghandler',
                      'gitpython',
                      'texttable'],
    package_data={"": ['*.toml']},
    include_package_data=True,
    entry_points="""
    [console_scripts]
    git996= git996.main:main
    """,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
