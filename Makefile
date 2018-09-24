clean:
	sudo python setup.py clean
	$(sudo pip uninstall rsatool <<< 'y')
	$(rm -rf `which rsatool` build dist)
	find . -name __pycache__ -exec rm -rf '{}' \;
	find . -name *.pyc -exec rm -rf '{}' \;
	find . -name *.egg* -exec rm -rf '{}' \;
	find . -name *cache -exec rm -rf '{}' \;

dev:
	sudo python setup.py develop

install:
	make clean
	sudo pip install -r requirements.txt
	sudo python setup.py install

test:
	python -m pytest