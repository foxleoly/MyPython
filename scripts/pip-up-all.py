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
import asyncio

"""
check the privillge, if non-root script will be exit.
if os.geteuid() != 0:
    print("This program must be run as root. Aborting.")
    sys.exit(1)

execute all the update commands.
"""
async def updatepip():
    """update pip lib"""
    for dist in pip.get_installed_distributions():
        call("sudo -H pip3 install -U " + dist.project_name, shell=True)

loop = asyncio.get_event_loop()
loop.run_until_complete(updatepip)
loop.close()
print("All the package updated.")
