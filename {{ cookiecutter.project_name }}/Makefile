.PHONY: docs
setup:
	rm -rf build
	rm -rf dist
	python setup.py bdist_wheel
dev:
	python setup.py develop
test:
	pytest tests -vvv
doc:
	rm -rf docs/_build && sphinx-apidoc -o docs {{ cookiecutter.project_name }} && cd docs && make html