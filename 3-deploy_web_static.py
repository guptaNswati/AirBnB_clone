#!/usr/bin/python3
"""
This module contains Fabric script that creates and distributes an archive
to the web servers, using the function deploy
"""
from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


env.user = 'ubuntu'
env.hosts = ['52.71.155.152', '184.72.141.74']


def deploy():
    """
    pack and deploy
    """
    try:
        return do_deploy(do_pack())
    except:
        return False
