#!/usr/bin/python3
"""
This module contains Fabric script that creates and distributes an archive
to the web servers, using the function deploy
"""
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """
    pack and deploy
    """
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)