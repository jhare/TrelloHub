# Basic fabfile structure. Need to fill it out.
from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm

def unittest():
    local("./nodeunit TODO")

def deploy():
    print("TODO")

def undeploy():
    print("TODO")

def github():
    local("git add -p && git commit")
    
def dropthehammer():
	unittest()
	github()
	undeploy()
	deploy()