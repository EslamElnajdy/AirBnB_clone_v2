#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from os.path import exists
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["54.209.195.60", "100.26.168.126"]


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.now()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(file_n, path, no_ext))
        run("rm /tmp/{}".format(file_n))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, no_ext))
        run("rm -rf {}{}/web_static".format(path, no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
