.PHONY: test

test:
	python -m unittest discover

clean:
	find . -name \*.pyc -delete
