.PHONY: init check format test coverage htmlcov requirements

init:
	pip install pipenv
	pipenv sync --dev

check:
	isort --recursive --check-only pythonsanicexample tests
	black -S -l 79 --check pythonsanicexample tests
	pylint pythonsanicexample

format:
	isort -rc -y pythonsanicexample tests
	black -S -l 79 pythonsanicexample tests

test:
	python -m pytest

coverage:
	python -m pytest --cov pythonsanicexample --cov-report term --cov-report xml

htmlcov:
	python -m pytest --cov pythonsanicexample --cov-report html
	rm -rf /tmp/htmlcov && mv htmlcov /tmp/
	open /tmp/htmlcov/index.html

requirements:
	pipenv lock -r > requirements.txt
	pipenv lock -dr > requirements-dev.txt
