from fabric.api import task, sudo, cd

@task
def start():
	"""
	BETA start the services. 
	TODO handle properly via packages/upstart.
	"""
	sudo("service redis-server start")

	with cd("/code/gachette"):
		sudo('GACHETTE_SETTINGS="/code/gachette/config.rc" celery -A gachette_web.tasks worker -l debug --purge >> /var/log/garnison.celery.log')
		sudo('GACHETTE_SETTINGS=/code/gachette/config.rc ./runserver.py >> /var/log/garnison.runserver.log')


@task
def stop():
	"""
	BETA start the services. 
	TODO handle properly via packages/upstart.
	"""
	sudo("service redis-server stop")
