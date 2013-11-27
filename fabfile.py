from fabric.api import env, local, run, task, cd, sudo, abort, settings

import caserne.garnison as garnison

@task
def vagrant():
    """
    Configure Fabric to connect to the vagrant instance
    """
 
    # get dictionary out of the vagrant ssh config
    result = local('vagrant ssh-config', capture=True)
    ssh_config = { line.split()[0] : line.split()[1].strip('"') for line in result.split("\n") }

    # configure fabric with the value from vagrant ssh-config
    env.user = ssh_config['User']
    env.hosts = ['%s:%d' % (ssh_config['HostName'], int(ssh_config['Port'])) ]
    env.key_filename = ssh_config['IdentityFile']

    env.forward_agent = True

    #local("vagrant up")

@task 
def uname():
    print "env.host_string: ", env.host_string
    run('uname -a')

@task
def setup():
    """
    Initial preparation.
    """
    setup_trebuchet()
    setup_gachette()
    setup_mise_a_feu()
    setup_garnison()

def setup_trebuchet():
    """
    Install trebuchet (packaging).
    """    
    prepare_git_clone("trebuchet", "git@github.com:ops-hero/trebuchet.git")
    sudo("pip install -e /code/trebuchet")
    run("trebuchet --version")

def setup_gachette():
    """
    Install gachette (build wrapper).
    """    
    prepare_git_clone("gachette", "git@github.com:ops-hero/gachette.git")
    sudo("pip install -e /code/gachette")
    run("gachette --version")

def setup_mise_a_feu():
    """
    Install mise-a-feu (deployment).
    """    
    pass

def setup_garnison():
    """
    Install garnison (web ui).
    """    
    pass


@task
def github():
    "test connection to github from within Fabric"
    run("ssh git@github.com")


def prepare_git_clone(name, repo):
    """
    Check if working copy is there and clone if not.
    """
    with settings(warn_only=True):
        if run("test -d /code/%s" % name).failed:
            with cd("/code"):
                run("git clone %s -o upstream" % repo)

output_dir = '/var/packages/debs'

packages = {
    'dh-secret-sauce':              'dh-secret-sauce-1.0.0-all.deb',
    'dh-secret-sauce-default':      'dh-secret-sauce-default-1.0.0-all.deb',
    'dh-secret-sauce-lib':          'dh-secret-sauce-lib-1.0.0-amd64.deb',
    'dh-secret-sauce-web-upstart':  'dh-secret-sauce-web-upstart-1.0.0-all.deb',
    'dh-secret-sauce-static':       'dh-secret-sauce-static-1.0.0-all.deb',
}

@task
def test_build_trebuchet():
    """
    Try to build the example applications of trebuchet (with clean up).
    """
    # build packages
    run("trebuchet build /code/trebuchet/example/application/.missile.yml --output %s --arch amd64" % output_dir)
    run("trebuchet build /code/trebuchet/example/product/secret_sauce.yml --output %s --arch amd64" % output_dir)

    # link nginx config file
    sudo("ln -f -s /etc/nginx/sites-available/secret_sauce_web_default.conf /etc/nginx/sites-enabled/secret_sauce_web_default.conf")

    # installation of packages
    with cd(output_dir):
        sudo("dpkg -i %s" % " ".join(packages.values()))

    # launch the instances
    sudo("start dh_secret_sauce_web_upstart_controller")

    # test
    run("/code/trebuchet/example/tests/test_curl.sh 0.0.0.0")

    # clean up
    sudo("rm /etc/nginx/sites-enabled/secret_sauce_web_default.conf")
    sudo("dpkg -r %s" % " ".join(packages.keys()))

@task
def test_build_gachette():
    """
    Try to build the example applications with gachette (FS) (with clean up).
    """
    # build packages
    run("gachette -H vagrant@0.0.0.0 prepare:test_config_first_build,git@github.com:ops-hero/test_config,master")
