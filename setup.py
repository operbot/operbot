# This file is placed in the Public Domain.


"setuptools"


import os


from setuptools import setup


def read():
    return open("README.rst", "r").read()


def uploadlist(dir):
    upl = []
    for file in os.listdir(dir):
        if not file or file.startswith('.'):
            continue
        d = dir + os.sep + file
        if os.path.isdir(d):   
            upl.extend(uploadlist(d))
        else:
            if file.endswith(".pyc") or file.startswith("__pycache"):
                continue
            upl.append(d)
    return upl


setup(
    name="operbot",
    version="111",
    author="Bart Thate",
    author_email="operbot100@gmail.com",
    url="http://github.com/operbot/operbot",
    description="write your own commands",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license="Public Domain",
    install_requires=["opr>=9"],
    packages=["operbot"],
    include_package_data=True,
    data_files=[
                ("operbot", ["files/operbot.service",]),
                ("share/doc/operbot", ["README.rst"])
               ],
    scripts=[
             "bin/operbot",
             "bin/operbotcmd",
             "bin/operbotctl",
             "bin/operbotd"
            ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: Public Domain",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: System Administrators",
        "Topic :: Communications :: Chat :: Internet Relay Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
     ],
)
