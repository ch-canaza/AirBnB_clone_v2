#!/usr/bin/python3
''' contains the function do_deploy '''
from fabric.api import env, sudo, run, put
from os.path import exists
env.hosts = ['35.237.244.23', '35.196.221.206']
env.user = 'ubuntu'


def do_deploy(archive_path):
    ''' distributes an archive to web servers '''
    if exists(archive_path) is False:
        return False
    file_name = archive_path.split('/')[-1]
    new = '/data/web_static/release/' + \
          "{}".format(file_name.split('.')[0])
    current = 'data/web_static/current'
    try:
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}/'.format(new))
        run('sudo tar -xzf {} -C {}/'.format(tmp, new))
        run('sudo rm /tmp/{}'.format(file_name))
        run('sudo mv {}/web_static {}/'.format(new))
        run('sudo rm -rf {}'.format(current))
        run('sudo ln -s {}/ {}'.format(new, current))
        return True
    except:
        return False

