.PHONY: all

all: help

help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {@printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

flake:  ## run flake8 check
	@~/.venv/bin/flake8  . || true
	@printf "*********** Flake check ended.\n\n\n"

black:  ## run black check
	@~/.venv/bin/black --diff .
	@printf "*********** Black check ended.\n\n\n"

isort:  ## run isort check
	@~/.venv/bin/isort --diff -rc .
	@printf "*********** Isort check ended.\n\n\n"

mypy:  ## run mypy check
	@~/.venv/bin/mypy --strict . || true
	@printf "*********** Mypy check ended.\n\n\n"
	# https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html#cheat-sheet-py3

check_all: flake black isort mypy  ## run all code checks
