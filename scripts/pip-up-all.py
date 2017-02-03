#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Leo Li
# Email: yaol.leo@gmail.com
"""
The script will update all the packages on the system.
"""
import sys
import os
from subprocess import call
import pip

"""
check the privillge, if non-root script will be exit.
"""
if os.geteuid() != 0:
    print("This program must be run as root. Aborting.")
    sys.exit(1)

"""
execute all the update commands.
"""

for dist in pip.get_installed_distributions():
    call("sudo -H pip3 install -U " + dist.project_name, shell=True)

print("All the package updated.")
