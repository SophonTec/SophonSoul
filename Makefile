SHELL := /bin/bash

all: setup init install test

init:
	@echo "Initiating the environment ..."

setup:
	sudo pip3 install pipenv
	sudo pipenv install

install:
	sudo pipenv install -e .

test:
	py.test tests -v

clean:
	@echo "Deleting *.pyc files ..."
	sudo -H find . -name "*.pyc" -type f -delete
	@echo "Deleting *.log files ..."
	sudo -H find . -name "*.log" -type f -delete
	@echo "Deleting *.png files ..."
	sudo -H find . -name "*.png" -type f -delete
	@echo "Deleting *.mp4 files ..."
	sudo -H find . -name "*.mp4" -type f -delete

showdiff: *.py
	@echo "This is the SophonSoul Project."
	git status
	git diff

help:
	@echo "setup:     install dependency packages and tools needed by sophoncore"
	@echo "init:      initialize the environment for sophoncore"
	@echo "install:   install the sophoncore as a python package"
	@echo "test:      run automatic unit tests of sophoncore"
	@echo "all:       perform all steps necessary for a new machine, install sophonecore package and run tests"
	@echo "clean:     clear the compiled binary code and logs"
	@echo "showdiff:  print local changes of source code"
	@echo "help:      show this help menu"

.PHONY: setup init install test clean showdiff help
