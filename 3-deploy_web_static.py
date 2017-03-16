#!/usr/bin/python3
"""
This module contains Fabric script that creates and distributes an archive
to the web servers, using the function deploy
"""


from time import strftime
from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ['52.71.155.152', '184.72.141.74']


def do_pack():
    """
    generates a .tgz archive of web_static folder files using fabrics local()
    """
    try:
        local("mkdir -p versions")
        created = "versions/web_static_{:s}.tgz".format(strftime
                                                        ("%Y%m%d%H%M%S"))
        local("tar -czvf {} web_static/".format(created))
        return created
    except:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to the web server using put
    """
    try:
        path, tar_file = os.path.split(archive_path)
        data_dir = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}{}/".format(data_dir, tar_file[:-4]))
        run("sudo tar -xzf /tmp/{} -C {}{}/".format(
            tar_file, data_dir, tar_file[:-4]))
        run("sudo rm /tmp/{}".format(tar_file))
        run("sudo mv {}{}/web_static/* {}{}/".format(
            data_dir, tar_file[:-4], data_dir, tar_file[:-4]))
        run("sudo rm -rf {}{}/web_static".format(data_dir, tar_file[:-4]))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}{}/ /data/web_static/current".format(
            data_dir, tar_file[:-4]))
        return True
    except:
        return False


def deploy():
    """
    pack and deploy
    """
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
