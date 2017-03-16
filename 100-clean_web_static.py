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
    with cd("/data/web_static/releases"):
        files = sudo("ls -tr").split(" ")
        files = [file for file in files if file != '']
        print(files)
        print(len(files))
        if len(files) > num:
            for file in files[:num]:
                print(file)
                run("sudo rm -rf {}".format(file))
