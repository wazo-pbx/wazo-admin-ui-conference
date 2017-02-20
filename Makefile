install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/conference.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-conference
	rm /etc/wazo-admin-ui/conf.d/conference.yml
	systemctl restart wazo-admin-ui
