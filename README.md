# Boilerplate backend flask

This is a basic boilerplate which provides a backend starter pack.

It use Python and the following technologies:

* Flask
* Pytest
* Flasgger

## How to install the boilerplate

At first, download the bundle after that and create a virtual environment and activate it (UNIX systems):
```{bash}
$ python3 -m venv venv
$ source venv/bin/activate
```

If you are using windows you should use the following commands:
```{windows}
$ python -m venv venv
$ venv\Scripts\activate
```

After that, install the needed packages with:
```{bash}
pip install requirements.txt 
```

### Run server
To run the server you need to use:
```{bash}
python application.py
```

### Run tests
To run the tests you have to use the following command:
```{bash}
python -m pytest -vvv
```