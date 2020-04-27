## HOW TO

* Install python3.7 or python3.8.

* Install virtualenv:
```bash
Get path of the python
> which python3

Then paste in here:
> virtualenv --python=/path/to/python3 ~/.venv

Or in one line:
virtualenv --python=$(which python3) ~/.venv
```

* Activate virtualenv:
```bash
source ~/.venv/bin/activate
```

* Install needed dependencies:
```bash
pip install -r requirements.txt
```

* Run linters and formatters:
```bash
> make check_all
```
