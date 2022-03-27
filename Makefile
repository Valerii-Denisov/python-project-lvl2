gendiff:
	poetry run gendiff

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

upgrade:
	python3 -m pip uninstall hexlet-code
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff
