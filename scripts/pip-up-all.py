#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Leo Li
# Email: yaol.leo@gmail.com
# Python version 3.6.5 test pass.
# pip upgrade to 10.0 use: 
# from pip._internal.utils.misc import get_installed_distributions
# the lib has changed.

"""
The script will update all the packages on the system.
"""

from subprocess import call
from multiprocessing import Process
import os
import pip


"""
execute all the update commands.
"""
def projname():
    """get the lib name by pip"""
    libname = []
    for dist in get_installed_distributions():
        libname.append(dist.project_name)
    return libname


def updatepip():
    """update pip lib"""
    for name in projname():
        call("sudo -H pip3 install -U " + name, shell=True)


if __name__ == '__main__':
    updatepip()
    print("All the packages updated.")
