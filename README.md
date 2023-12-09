# daftar-common

## Description
daftar-common contains all the bricks you need to create a functionnal data science project.

## Requirements
The requirements for the project are the following:  
- python3.6+
- make command
    - For windows users, you can download make command following this [link](https://sourceforge.net/projects/gnuwin32/files/make/3.81/make-3.81.exe/download?use_mirror=netix&download=). For more details on other versions, follow [this page](https://gnuwin32.sourceforge.net/packages/make.htm)
    - For linux/mac users, download make command following your ``sudo apt-get update & apt-get -y install make``   

To check make is correctly installed, type ``make --version``

## Setup the environment
Start by running ``make--version`` and ``python --version`` to make sure you have all the prerequists.     

- Run ``make setup``
- activate your environement :
    - Windows: .\wenv\Scripts\activate
    - Linux:   ./venv/bin/activate
- Start developping !

PS: To check that you're on the right envrionnement, type ``python -m daftar_common.src.main``.



## Dev tools available:

Those command are targeting the **daftar_common** folder and the configuration is [here](setup.cfg).

* Code Quality: You can trigger those commands with `make check`.
  * **Formatting** with `black + isort`: To format use ``make format`` and check with `make black` and `make isort` for `black` and `isort` respectively
  * **type-checking** with `mypy`: You can use `make mypy` to check the types and detect errors
  * **Linting** with `flake8 + pylint`: You can use `make flake8` and `make pylint` to lint your code using `flake8` and `pylint` respectively.
* Tests:
  * For testing we use `pytest` and target the tests in the **daftar_common** using `make test`
  * You can generate a coverage report using `make coverage` and a html version using `make coverage-html`