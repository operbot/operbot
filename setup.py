# This file is placed in the Public Domain.


from setuptools import setup


def read():
    return open("README.rst", "r").read()


setup(
    name="operbot",
    version="100",
    author="Bart Thate",
    author_email="operbot100@gmail.com",
    url="http://github.com/operbot/operbot",
    description="operator bot",
    long_description=read(),
    license="Public Domain",
    packages=["op", "oper", "operbot", "opermod"],
    scripts=["bin/op", "bin/operbot"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python",
        "Intended Audience :: System Administrators",
        "Topic :: Communications :: Chat :: Internet Relay Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
     ],
)
