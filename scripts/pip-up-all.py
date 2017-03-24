#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Leo Li
# Email: yaol.leo@gmail.com
# Python version 3.6.0 test pass.
"""
The script will update all the packages on the system.
"""

from subprocess import call
import pip

"""
execute all the update commands.
"""
def projname():
    """get the lib name by pip"""
    libname = []
    for dist in pip.get_installed_distributions():
        libname.append(dist.project_name)
    return libname


def updatepip():
    """update pip lib"""
    for i in projname():
        call("sudo -H pip3 install -U " + i, shell=True)


if __name__ == '__main__':
    updatepip()
    print("All the package updated.")
