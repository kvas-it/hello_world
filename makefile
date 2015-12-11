.PHONY: devenv clean install uninstall test testcov htmlcov

MODULE=hello_world
DEVENV=__
TESTS=tests

PYTHON=${DEVENV}/bin/python
PIP=${DEVENV}/bin/pip
PYTEST=${DEVENV}/bin/py.test
TOX=${DEVENV}/bin/tox

help:
	@echo
	@echo "    Usage: make <target>"
	@echo
	@echo "Where target is one of:"
	@echo
	@echo "    devenv    -- Create development environment"
	@echo "    test      -- Run the tests with default version of python"
	@echo "    testcov   -- Output test coverage report to console"
	@echo "    htmlcov   -- Generate test coverage report in HTML"
	@echo "    testall   -- Run the tests with all supported python versions"
	@echo "    install   -- Install module and script with default python"
	@echo "    uninstall -- Uninstall from default python"
	@echo "    clean     -- Remove testing and build artifacts"
	@echo

devenv: ${DEVENV}

${DEVENV}:
	virtualenv ${DEVENV}
	${PIP} install pytest pytest-cov tox
	${PYTHON} setup.py develop

test: ${DEVENV}
	${PYTEST} ${TESTS}

testcov: ${DEVENV}
	${PYTEST} --cov=${MODULE} ${TESTS}

htmlcov: ${DEVENV}
	${PYTEST} --cov-report=html --cov=${MODULE} ${TESTS}

testall: ${DEVENV}
	${TOX}

install:
	python setup.py install

uninstall:
	pip uninstall -y ${MODULE}

clean:
	rm -Rf ${DEVENV} .coverage .cache .tox htmlcov ${MODULE}.egg-info\
		`find . -name *.pyc` build dist MANIFEST
