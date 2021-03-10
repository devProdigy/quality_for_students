# Code quality checks example for students

# Table of Contents
* [Setup project](#Setup-project)
    * [Install Poetry and Invoke](#Install-Poetry-and-Invoke)
    * [Setup Virtual Environment](#Setup-Virtual-Environment)
* [Automated Tasks](#Automated-Tasks)
  * [Run tests](#Run-tests)
  * [Run code quality checks](#Run-code-quality-checks)
  * [Run safety checks for project libraries](#Run-safety-checks-for-project-libraries)
  * [Run project code](#Run-project-code)

## Setup project

### Install Poetry and Invoke
This project uses [invoke](http://www.pyinvoke.org/) and 
[poetry](https://python-poetry.org/) to speed up the process.

You need to install them only once.

The simplest way to get both is to install [poetry](https://python-poetry.org/)
first, with the officially recommended way:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
You may need to run following command then:
```
echo 'export PATH="$PATH:$HOME/.poetry/bin"' >> $HOME/.zshrc
```

(Check out alternative instructions for `poetry` installation 
[here](https://python-poetry.org/docs/#installation))

After that [poetry](https://python-poetry.org/) is able to automatically
provide you with `invoke` installed in the project virtual env.  
So you can do one of following [task](#Automated-Tasks):
```
# Run it directly
poetry run inv [task]

# Run it from the virtual environment
poetry shell
inv [task]

# Have an alias (use custom name to avoid clashing with `inv` and `invoke`)
alias invv='poetry run inv'
invv [task]
```

An alternative way to install all tools is using 
[pipx](https://pipxproject.github.io/pipx/):

```
python3.7 -m pip install pipx --user
pipx install poetry
pipx install invoke
```

### Setup Virtual Environment
Run `poetry install` to install or re-install all dependencies.  
Now you should have fully setup local environment to run the project. 

If needed: run `poetry update` to update the locked dependencies to the most recent
version, honoring the constrains put inside `pyproject.toml`.


##Automated Tasks

### Run tests
```shell
poetry run inv test
```

### Run code quality checks
```shell
poetry run inv code-check
```

### Run safety checks for project libraries
```shell
poetry run inv check-safety
```

### Run project code
```shell
poetry run inv run-app
```
