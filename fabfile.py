import os,sys,logging,time
from fabric.state import env
from fabric.api import env,local,run,sudo,put,cd,lcd,puts,task,get,hide
from settings import BUCKET_NAME,DATA_PATH,INDEX_PATH
from settings import USER,private_key,HOST
env.user = USER
env.key_filename = private_key
env.hosts = [HOST,]
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='logs/fab.log',
                    filemode='a')

@task
def connect():
    """
    Creates connect.sh for the current host
    :return:
    """
    fh = open("connect.sh",'w')
    fh.write("#!/bin/bash\n"+"ssh -i "+env.key_filename+" "+"ubuntu"+"@"+HOST+"\n")
    fh.close()


@task
def clear():
    """
    delete logs
    """
    local('rm logs/*.log &')

@task
def setup():
    """
    """
    sudo("chmod 777 /mnt/")
    sudo("add-apt-repository ppa:kirillshkrogalev/ffmpeg-next")
    sudo("apt-get update")
    sudo("apt-get install -y ffmpeg")
    sudo("pip install fabric")
    sudo("pip install --upgrade awscli")
    sudo("pip install --upgrade fabric")
    sudo("pip install --upgrade flask")
    sudo("pip install --upgrade ipython")
    sudo("pip install --upgrade jupyter")
    sudo("apt-get install -y libblas-dev liblapack-dev libatlas-base-dev gfortran")
    sudo("pip install --upgrade nearpy")
    sudo

@task
def process():
    with cd("image-analogies"):
        run("THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 python image_analogy.py images/arch-mask.jpg images/arch.jpg images/arch-newmask.jpg out/arch")