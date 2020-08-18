#!/usr/bin/python3
"""generates compiled archive from AirBnB clone."""
from datetime import datetime
from fabric.operations import local


def do_pack():
    """generates the comppressed archive"""
    File_name = "versions/web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    result = local("tar -zcvf versions/{} web_static".format(File_name))

    if result.failed:
        return None
    return File_name
