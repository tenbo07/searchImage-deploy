from fabric.api import sudo,cd,put
import cuisine

def upload():
    put('./searchImage.conf', '/tmp/')

def start_app():
    sudo('initctl start searchImage')

def go_app_deploy():
    upload()
    with cd('/usr/local/gocode/src'):
      sudo("rm -rf searchImage")
      sudo("git clone https://github.com/tenbo07/searchImage.git")
    with cd('/tmp'):
      sudo('rm -f /etc/init/searchImage.conf')
      sudo('mv searchImage.conf /etc/init/')
    start_app()
