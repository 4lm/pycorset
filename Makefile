init:
	pipenv install
install:
	pipenv run python setup.py install
test:
	pipenv run pytest --pylint --codestyle --cov=pycorset
	rm coverage.svg
	pipenv run coverage-badge -o coverage.svg
	pipenv run mypy pycorset