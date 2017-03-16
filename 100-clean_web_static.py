#!/usr/bin/python3
"""
This module contains Fabric script that creates and distributes an archive
to the web servers, using the function deploy
"""
from fabric.api import *
env.user = 'ubuntu'
env.hosts = ['52.71.155.152', '184.72.141.74']


def do_clean(number=0):
    """
    clean local archive and server
    """
    num = int(number)
    if num == 0:
        num += 1
    files = local("ls -tr versions", capture=True).split("\n")
    if len(files) > num:
        for file in files[:num]:
            local("rm -f versions/{}".format(file))
    dir_toclean = ""
    with cd("/data/web_static/releases"):
        files = sudo("ls -tr").split("\r\n")
    files = [file for file in files if "web_static" in file]
    if len(files) > num:
        for file in files[:num]:
            run("sudo rm -rf /data/web_static/releases/{}".format(file))