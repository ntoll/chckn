XARGS := xargs -0 $(shell test $$(uname) = Linux && echo -r)
GREP_T_FLAG := $(shell test $$(uname) = Linux && echo -T)
export PYFLAKES_BUILTINS=_

all:
	@echo "\nChicken chicken chicken chicken CHICKEN chicken. Chicken:\n"
	@echo "make clean - chicken chicken chicken chicken chicken chicken."
	@echo "make tidy - chicken chicken 'chicken' chicken."
	@echo "make docs - chicken CHICKEN chicken."
	@echo "make dist- chicken chicken."
	@echo "make chicken - chicken CHICKEN chicken."

clean:
	rm -rf chckn.egg-info
	rm -rf .pytest_cache
	rm -rf docs/_build
	rm -rf .eggs
	rm -rf build
	rm -rf dist
	find . \( -name '*.py[co]' -o -name dropin.cache \) -delete
	find . \( -name '*.bak' -o -name dropin.cache \) -delete
	find . \( -name '*.tgz' -o -name dropin.cache \) -delete
	find . | grep -E "(__pycache__)" | xargs rm -rf

tidy: clean
	@echo "\nChicken chicken chicken..."
	black -l 79 chicken.py 

docs: clean
	$(MAKE) -C docs html
	@echo "\nChicken CHICKEN chicken:"
	@echo file://`pwd`/docs/_build/html/index.html
	@echo "\n"

dist: clean
	@echo "\nChicken chicken chicken chicken chicken chicken..."
	python setup.py sdist bdist_wheel

chicken: dist
	@echo "\nChicken CHICKEN... chicken CHICKEN chicken..."
	twine upload --sign dist/*
