#!/usr/bin/python3
from fabric.api import put, run, env
from os.path import exists, join

env.hosts = ["100.26.168.126", "54.209.195.60"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not exists(archive_path):
        print(f"Error: Archive '{archive_path}' does not exist.")
        return False

    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        
        run("sudo mkdir -p /data")
        run("sudo chown -R ubuntu:ubuntu /data")
        
        # Upload archive
        put(archive_path, "/tmp/")
        
        # Create directory for release
        run(f"mkdir -p {join(path, no_ext)}")
        
        # Extract archive
        run(f"tar -xzf /tmp/{file_name} -C {join(path, no_ext)}")
        
        # Clean up
        run(f"rm /tmp/{file_name}")
        
        # Move files
        run(f"mv {join(path, no_ext)}/web_static/* {join(path, no_ext)}/")
        
        # Remove unnecessary folder
        run(f"rm -rf {join(path, no_ext)}/web_static")
        
        # Update symbolic link
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {join(path, no_ext)}/ /data/web_static/current")

        print("Deployment successful!")
        return True
    except Exception as e:
        print(f"Error during deployment: {e}")
        return False
