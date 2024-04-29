all: test

install: venv

test: install
	pytest -s tst/ --cov-fail-under=100 --cov=src --cov-report=html

clean:
	if exist .coverage del .coverage
	if exist venv\ rmdir /s /q venv
	if exist htmlcov\ rmdir /s /q htmlcov
	if exist .pytest_cache\ rmdir /s /q .pytest_cache
	for /r /d %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d" 2>nul

venv: requirements.txt
	python -m venv venv
	pip install -r requirements.txt

.PHONY: all install run clean test