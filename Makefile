all: install

install: venv

run: install
	python src/main.py

clean:
	if exist venv\ rmdir /s /q venv
	del /S *.pyc 2>nul

venv: requirements.txt
	python -m venv venv
	pip install -r requirements.txt

.PHONY: all install run clean