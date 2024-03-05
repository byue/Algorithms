all: test

install: venv

test: install
	pytest tst/ -s

clean:
	if exist venv\ rmdir /s /q venv
	for /r /d %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d" 2>nul

venv: requirements.txt
	python -m venv venv
	pip install -r requirements.txt

.PHONY: all install run clean test