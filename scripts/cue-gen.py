#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Leo Li
# Email: yaol.leo@gmail.com
"""
The script will generate cue file automaticly.
"""
import os
import re
import mutagen


def readfileinfo(file):
    file = mutagen.File(file)
    return file, file['artist'], file['title'], file['album']

def cuegenerate():
    return

filelist = os.listdir('.')
flacres = []
for names in filelist:
    if names.endswith('.flac'):
        flacres.append(names)
