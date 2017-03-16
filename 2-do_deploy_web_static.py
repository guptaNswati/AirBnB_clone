#!/usr/bin/python3
"""
This module contains a Fabric script that distributes an archive to the web
servers, using the function do_deploy
"""
from time import strftime
from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ['52.71.155.152', '184.72.141.74']


def do_deploy(archive_path):
    """
    distributes an archive to the web server using put
    """
    try:
        path, tar_file = os.path.split(archive_path)
        with cd("/tmp"):
            put("{}".format(archive_path), "{}".format(tar_file))
            run("tar -xzvf {} /data/web_static/releases/{}".format(
                tar_file, tar_file[:-4]))
            run("rm -f {}".format(tar_file))
        run("rm -f /data/web_server/current")
        run("ln -s  /data/web_static/releases/{} /data/web_server/current".
            format(tar_file[:-4]))
        return True
    except:
        return False
