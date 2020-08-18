#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
"""
from fabric.api import local, run, put, env, hosts, env
import os.path
from datetime import datetime

env.hosts = ['35.231.195.75', '52.91.219.244']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ that distributes an archive to your web servers, using
    the function do_deploy:"""

    if not archive_path:
        return false
    file_second_arg = archive_path.split("/")[-1]
    new_file = "/data/web_static/release/" + "{}".format(file_second_arg
                                                         .split(".")[0])
    current_path = "data/web_static/current"
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(new_file))
        run("sudo tar -zxf /tmp/{} -C {}".format(file_second_arg, new_file))
        run("sudo rm /tmp/{}".format(file_second_arg))
        run("sudo mv {}/web_static {}/".format(new_file))
        run("sudo rm -rf {}".format(current_path))
        run("sudo ln -s {} {}".format(new_file, current_path))
        return True
    except:
        return False
