# ORC Plugin

[![Python
version](https://img.shields.io/badge/python-v3.10-blue)](.coverage/html/index.html)
[![FastAPI
version](https://img.shields.io/badge/fastapi-v0.78.0-blue)](.coverage/html/index.html)
[![Coverage](.badges/coverage-badge.svg)](.coverage/html/index.html)

---

## Local development

To develop the service locally you need:

- python 3.10

A virtual environment is a Python tool for dependency management and project
isolation. For further info about the creation and management of a virtual environment,
please check the [Python official documentation](https://docs.python.org/3/library/venv.html).
To activate your virtual envirorment run the following command on
your terminal:

```shell
source /path/to/virtual/environment/bin/activate
```

When finished, to deactive the virtual envirorment run the following
command:

```shell
deactivate
```

Once you have the virtual environment in place, you need to install the
dependencies listed in *requirements.txt* file:

```shell
pip install -r requirements.txt
```

During development, you will probably have to perform the same operations many
times: start the application locally, check the code quality, run tests and compute coverage. Therefore,
to avoid to remember each time the syntax of the commands to be executed, the
main commands were collected in a Makefile. [Makefile](https://www.gnu.org/software/make/manual/make.html) is a Unix automation tool
that contains the recipe to build and run your program. So, listed below are the
commands that can be executed by the make command:

Run application locally:
```shell
make start
```

Run linter for code quality:
```shell
make lint
```

Run tests:
```shell
make test
```

Compute the coverage:
```shell
make coverage
```

---