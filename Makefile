#!/usr/bin/env make

# Change this to be your variant of the python command
PYTHON ?= python # python3 py

all:
# ---------------------------------------------------------
# Setup a venv and install packages.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc:
	rm -rf docs

clean-src:
	$(call FOREACH,clean)

clean-all:
	clean clean-doc clean-src
	rm -rf .venv



# ---------------------------------------------------------
# Generating documentaion.
#
.PHONY:
	pydoc

pdoc:
	@$(call MESSAGE,$@)
	pdoc player.py -o ./docs
	pdoc dice.py -o ./docs
	pdoc bot.py -o ./docs
	pdoc singleplayer.py -o ./docs
	pdoc multiplayer.py -o ./docs
	pdoc chooseGameMode.py -o ./docs
	pdoc main.py -o ./docs
	pdoc test_player.py -o ./docs
	pdoc test_dice.py -o ./docs
	pdoc test_bot.py -o ./docs
	pdoc test_singleplayer.py -o ./docs
	pdoc test_multiplayer.py -o ./docs
	pdoc test_chooseGameMode.py -o ./docs

pyreverse:
	@$(call MESSAGE,$@)
	install -d docs/pyreverse
	pyreverse bot.py
	pyreverse player.py
	pyreverse dice.py
	pyreverse singleplayer.py
	pyreverse multiplayer.py
	pyreverse chooseGameMode.py
	pyreverse main.py
	dot -Tpng classes.dot -o classes.png

	dot -Tpng classes.dot -o docs/pyreverse/classes.png
	dot -Tpng packages.dot -o docs/pyreverse/packages.png
	rm -f classes.dot packages.dot

doc:
	pdoc pyreverse #pydoc sphinx
# ---------------------------------------------------------
# Unittesting and coverage.
#
coverage:
	coverage run -m unittest
	coverage report
	coverage html

unittest:
	$(PYTHON) -m unittest discover -v
# ---------------------------------------------------------
# Test all the code at once.
#
pylint:
	$(call FOREACH,pylint)

flake8:
	$(call FOREACH,flake8)

lint: flake8 pylint

test:
	$(call FOREACH,test)
