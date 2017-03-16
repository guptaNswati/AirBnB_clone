#!/usr/bin/python3
"""
This module contains a Fabric script that generates a .tgz archive from the
contents of the web_static folder.
"""
from time import strftime
from fabric.api import *
from fabric.contrib import files
import os

def do_deploy(archive_path):
    #if fabric.contrib.files.exists(archive_path, use_sudo=False, verbose=False):
    try:
        #env.user = 'ubuntu'
        env.hosts = ['52.71.155.152', '184.72.141.74']
        path, tar_file = os.path.split(archive_path)
        with cd("/tmp"):
            put("{}".format(archive_path), "{}".format(tar_file))
            run("tar -xzvf {} /data/web_static/releases/{}".format(
                tar_file, tar_file[:-4]))
            run('rm -f {}'.format(tar_file))
        run('rm -f /data/web_server/current')
        run('ln -s  /data/web_static/releases/{} /data/web_server/current'.
            format(tar_file[:-4]))
        return True
    except:
        return False
