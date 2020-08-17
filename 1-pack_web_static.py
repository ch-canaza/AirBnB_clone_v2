#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
     from the contents of the web_static folder of
     your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
import os.path
from datetime import datetime


def do_pack():
    """ script that generates a .tgz archive
    from the contents of the web_static"""
    date_now = datetime.utcnow()
    file_date_format = "versions/web_static_{}{}{}{}{}{}.tgz".format(
                                                        date_now.year,
                                                        date_now.month,
                                                        date_now.day,
                                                        date_now.hour,
                                                        date_now.minute,
                                                        date_now.second)
    local("sudo mkdir -p versions")
    local("sudo tar -cvzf {} web_static".format(file_date_format))
    
    return file_date_format
