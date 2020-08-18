#!/usr/bin/python3
"""generates compiled archive from AirBnB clone"""
from datetime import datetime
from os import path
import ntpath
from fabric.operations import local, put, run
from fabric.api import env


env.hosts = ['35.243.171.126, 35.231.185.188']


def do_pack():
    """generates the comppressed archive"""
    local("mkdir -p versions")
    result = local("tar -zcvf versions/web_static_{}.tgz web_static".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))

    if result.failed:
        return None
    return result


def do_deploy(archive_path):
    """function to deploy"""
    if not path.exists(archive_path):
        return False
    try:
        h, t = ntpath.split(archive_path)
        if t:
            archive = t
        else:
            archive = ntpath.basename(h)
        h, t = ntpath.splitext(archive)
        if h:
            name = h
        else:
            name = ntpath.basename(h)

        put(archive_path, "/tmp/{}".format(archive))
        run("sudo mkdir -p /data/web_static/releases/{}/".format(name))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive, name))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
                            /data/web_static/releases/{}/"
            .format(name, name))
        run("sudo rm /tmp/{}".format(archive))
        run("sudo rm -rf /data/web_static/current")
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(name))
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        print("New version deployed!")

    except Exception:
        return False
