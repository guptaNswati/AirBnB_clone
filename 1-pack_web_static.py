#!/usr/bin/python3
"""
This module contains a Fabric script that generates a .tgz archive from the
contents of the web_static folder.
"""
from time import strftime
from fabric.api import *

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
