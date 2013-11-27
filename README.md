Caserne
=======

    casern, caserne [kəˈzɜːn]
    noun
    (Military) (formerly) a billet or accommodation for soldiers in a town

`Caserne` is a virtual machine to test the deployment scripts/library like `trebuchet`, `gachette`, `mise-a-feu` and the web UI `garnison`.


Installation
------------

- download and install vagrant from http://downloads.vagrantup.com/.
- download and install virtualbox ( > v4.2.14) from: https://www.virtualbox.org/wiki/Downloads

- $ git clone git@github.com:ops-hero/caserne.git
- $ cd caserne
- Check Vagrantfile configuration, especially the ip (config.vm.network) and the location of the project folder (config.vm.share_folder "v-code")
- $ vagrant up

- install virtualenv and virtualenvwrapper from: http://www.doughellmann.com/projects/virtualenvwrapper/
- $ mkvirtualenv caserne
- $ pip install -r requirements.pip
- $ fab vagrant uname
- $ fab vagrant github
- $ fab vagrant setup


Note
----

* You should have a folder that contains all the projects you need to work on, this should be setup for the Vagrant share folder (config.vm.share_folder "v-code"), so that it is available within the virtual machine.
* If the project is not present, Bidasse will clone the project from github and proceed as normal.

Todo
----
* Setup command to create Vagrantfile from template (to handle different IP, project folder).
* Add a setup.py file to use `caserne` from command line.
* Installation of the packages via `mise-a-jour`.
* Build different version/commits/branch via `gachette`.
* Use different version of deployment tool; `trebuchet`, `gachette`, `mise-a-jour`.
* Deploy the `garnison` web interface to control build and deployment.