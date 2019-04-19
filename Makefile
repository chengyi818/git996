# Author: ChengYi
# created time: Fri 19 Apr 2019 08:51:26 PM CST
# 1. make dep
#   install and upgrade dependency
# 2. make release
#   generate release package
# 3. upload to pypi
#
# 4. uninstall:
#   remove installed files

dep:
	python3 -m pip install --user --upgrade setuptools wheel
	python3 -m pip install --user --upgrade twine

release:
	rm -rf build/ dist/ git996.egg-info/
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*

install:
	python3 setup.py install --user

uninstall:
	python3 setup.py install --user --record log
	cat log | xargs rm -rf
