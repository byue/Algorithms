SHELL := /usr/bin/env bash

.SHELLFLAGS := -e -c

ifdef GITHUB_ACTIONS
  IS_GITHUB_ACTIONS := true
else
  IS_GITHUB_ACTIONS := false
endif

ifeq ($(OS),Windows_NT)
    PYTHON := python
	ifeq ($(IS_GITHUB_ACTIONS), true)
		VENV_PYTHON_PATH := venv/Scripts/python
	else
		VENV_PYTHON_PATH := venv\Scripts\python
	endif
else
    PYTHON := $(shell which python3 || which python)
	VENV_PYTHON_PATH := venv/bin/python
endif

all: test

install: check_python venv

check_python:
	@$(PYTHON) --version || (echo "Python3 is not installed. Please install" && exit 1)

test: install
ifeq ($(OS),Windows_NT)
	$(VENV_PYTHON_PATH) -m pytest -s tst/ --cov-fail-under=100 --cov=src --cov-report=html
else
	$(VENV_PYTHON_PATH) -m pytest -s tst/ --cov-fail-under=100 --cov=src --cov-report=html
endif

clean:
ifeq ($(OS),Windows_NT)
	if exist .coverage del .coverage
	if exist venv\ rmdir /s /q venv
	if exist htmlcov\ rmdir /s /q htmlcov
	if exist .pytest_cache\ rmdir /s /q .pytest_cache
	for /r /d %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d" 2>nul
else
	if [ -f .coverage ]; then rm .coverage; fi
	if [ -d venv ]; then rm -rf venv; fi
	if [ -d htmlcov ]; then rm -rf htmlcov; fi
	if [ -d .pytest_cache ]; then rm -rf .pytest_cache; fi
	find . -type d -name '__pycache__' -exec rm -rf {} +
endif

venv: requirements.txt
	$(PYTHON) -m venv venv
ifeq ($(OS),Windows_NT)
	$(VENV_PYTHON_PATH) -m pip install -r requirements.txt
else
	$(VENV_PYTHON_PATH) -m pip install -r requirements.txt
endif

.PHONY: all install run clean test