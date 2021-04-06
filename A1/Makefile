PY = python3
PYFLAGS = 
PYTEST = pytest
DOC = doxygen
DOCFLAGS = 
DOCCONFIG = docConfig

SRC = src/test_driver.py
PARTNER = partner/test_driver.py
SRCEXPT = src/test_expt.py

.PHONY: all test doc clean

test: 
	$(PY) $(PYFLAGS) $(SRC)

expt: 
	$(PY) $(PYFLAGS) $(SRCEXPT)

doc: 
	$(DOC) $(DOCFLAGS) $(DOCCONFIG)
	cd latex && $(MAKE)
part:
	$(PY) $(PYFLAGS) $(PARTNER)

all: test doc

clean:
	rm -rf html
	rm -rf latex
